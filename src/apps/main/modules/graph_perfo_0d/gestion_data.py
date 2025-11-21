import pandas as pd
from bsamreader import ThroughFlow
import h5py
import re
import os
from datetime import datetime
import numpy as np
from typing import Dict, List

from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side

from django.conf import settings
from django.template import Context, Template

from apps.main.models import Cas, IsoVitesse, RowPair, Row
from apps.main.modules.graph_perfo_0d.get_config_from_row import \
    get_row_from_antarescard, define_config_list, \
    read_input_file, get_flux_alias, rename_row


def export_data_html(data, etat):
    # Générer le nom de fichier avec la date actuelle
    html_filepath = os.path.join(etat.work_directory, f"{settings.PERFOS0D_EXPORT_NAME}.html")

    template_path = os.path.join(
        settings.BASE_DIR, "apps", "templates", "trunks", "base_graph_export.html"
    )
    # Charger et lire le template HTML
    with open(template_path, encoding="utf-8") as file:
        template = Template(file.read())

    # Rendre le contenu avec les données
    data["etat"] = etat.name
    data["projet"] = etat.projet
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["date"] = current_date
    data["created_by"] = etat.projet.created_by
    context = Context(data)
    rendered_content = template.render(context)

    # Sauvegarder le contenu HTML dans un fichier externe
    with open(html_filepath, "w", encoding="utf-8") as output_file:
        output_file.write(rendered_content)

    print(f"Export Fichier HTML --> {html_filepath}")


def export_data_excel(data, etat):
    data_all = {}
    for index, etage in enumerate(list(data.keys())):
        frames = [df for df in data[etage].values() if not df.empty and not df.isna().all().all()]
        data_all[etage] = pd.concat(frames, ignore_index=True)

    excel_filepath = os.path.join(etat.work_directory, f"{settings.PERFOS0D_EXPORT_NAME}.xlsx")

    column_to_mask = ['element_color', 'id', 'marker', 'is_only_stator']
    colors_by_sheet = {}

    with pd.ExcelWriter(excel_filepath) as writer:
        for sheet, df in data_all.items():
            colors = df['element_color'].tolist() if 'element_color' in df.columns else ['#000000'] * len(df)
            colors_by_sheet[sheet] = colors

            column_to_mask_exist = [col for col in column_to_mask if col in df.columns]
            df = df.drop(columns=column_to_mask_exist)
            cols = df.columns.tolist()
            if 'name' in cols:
                cols.insert(0, cols.pop(cols.index('name')))
            if 'data_type' in cols:
                cols.insert(1, cols.pop(cols.index('data_type')))
            df = df[cols]
            df.to_excel(writer, sheet_name=sheet, index=False)

    border = Border(
        left=Side(style='thin', color='000000'),
        right=Side(style='thin', color='000000'),
        top=Side(style='thin', color='000000'),
        bottom=Side(style='thin', color='000000')
    )

    wb = load_workbook(excel_filepath)
    for sheet, colors in colors_by_sheet.items():
        ws = wb[sheet]
        fill_head = PatternFill(start_color='D3D3D3', end_color='D3D3D3', fill_type='solid')
        for cell in ws[1]:
            cell.fill = fill_head
            cell.border = border

        for row_num, couleur in enumerate(colors, start=2):
            if isinstance(couleur, str) and couleur.startswith("#") and len(couleur) == 7:
                hexcolor = couleur.replace("#", "")
                font = Font(color=hexcolor)
            else:
                font = None
            for cell in ws[row_num]:
                if font:
                    cell.font = font
                cell.border = border
    wb.save(excel_filepath)

    print(f"Export Fichier Excel --> {excel_filepath}")

def set_data_row(cas):

    antarescard_filepath = os.path.join(cas.repertory, "calculation/carte_antares.py")

    config_dico = read_input_file(antarescard_filepath)

    row_data = {}

    for grid_key, grid_val in config_dico['gridFields'].items():
        row_data[grid_key] = {
            "flux": get_flux_alias(grid_val['Flux'], data_type='cfd'),
            "position": grid_val['FluxIndex'],
            "omega": grid_val['Omega'],
            "nb_blade": grid_val['TotalBladeCount'],
            "bsam_name": grid_val['GridBSAMName']
        }

    cas.row_metadata = row_data
    cas.save()

def set_inlet_outlet_row_obj(case_obj, rowpair_obj):

    pair_row_name_split = rowpair_obj.name.split("-")

    if len(pair_row_name_split) == 1:
        row_amont, row_aval = pair_row_name_split[0], pair_row_name_split[0]
    else:
        row_amont, row_aval = pair_row_name_split[0], pair_row_name_split[1]
    print(case_obj, row_amont, row_aval)

    rowpair_obj.entry_row = Row.objects.get(cas=case_obj, name=row_amont)
    rowpair_obj.exit_row = Row.objects.get(cas=case_obj, name=row_aval)
    rowpair_obj.save()


def extract_average_values(hdfMoy, r_gaz, cp) -> Dict[str, float]:
    extracted = {}
    for var in ["Pta", "Tta", "Q", "Ps", "Ptr"]:
        if var not in hdfMoy:
            rho = hdfMoy['Density'][()][0]
            if "V" not in hdfMoy:
                vx = hdfMoy['MomentumX'][()][0] / rho
                vy = hdfMoy['MomentumY'][()][0] / rho
                vz = hdfMoy['MomentumZ'][()][0] / rho
                v = np.sqrt(vx ** 2 + vy ** 2 + vz ** 2)
            else:
                v = hdfMoy['V'][()][0]

            Et = hdfMoy['EnergyStagnationDensity'][()][0] / rho
            ea = Et - 0.5 * v ** 2
            ts = ea / (cp - r_gaz)
            ps = rho * r_gaz * ts
            hs = ts * cp
            ht = hs + 0.5 * v ** 2
            tt = ht / cp
            match var:
                case "Ps":
                    extracted[var] = ps
                case "Tta":
                    extracted[var] = tt
        else:
            extracted[var] = hdfMoy[var][()][0]

    return extracted

def process_grid(grid, grid_name: str) -> List[Dict]:
    results = []

    grid_name_bsam = str(grid["BSAM_NAME"][()].decode())
    grid_omega = grid["Omega"][()]
    r_gaz = grid["Rgaz"][()]
    cp = grid["polynomeCoeff"][()][0]
    gamma = cp / (cp - r_gaz)

    if "BSAM_Cuts" not in grid:
        return results

    for plane_name in ['Inlet', 'Outlet']:
        if "inlet" in plane_name.lower() or "outlet" in plane_name.lower():
            plane_hdf = grid["BSAM_Cuts"][plane_name]

            if grid_name and grid_name.startswith('2.'):
                grid_flow = "Secondaire"
            elif grid_name and grid_name.startswith('3.'):
                grid_flow = "Primaire"
            else:
                grid_flow = "Total"

            flow = None
            if 'BSAM_' in plane_name:
                n_flow = plane_name.split('BSAM_')[-1].split('_')[0]
                flow = {"1": "Total", "2": "Secondaire", "3": "Primaire"}.get(n_flow)
            elif '_Prim' in plane_name:
                flow = "Primaire"
            elif '_Sec' in plane_name:
                flow = "Secondaire"
            elif plane_name.startswith('1.'):
                flow = "Total"
            elif plane_name.startswith('2.'):
                flow = "Secondaire"
            elif plane_name.startswith('3.'):
                flow = "Primaire"

            grid_flow_name = flow if flow else grid_flow

            for instant in plane_hdf:
                plane_instant_hdf = plane_hdf[instant]
                if "Average" not in plane_instant_hdf:
                    continue

                plane_instant_0d_hdf = plane_instant_hdf["Average"]

                for moy_0d in ["Moyenne_type_5"]:
                    if moy_0d in plane_instant_0d_hdf:
                        hdfMoy = plane_instant_0d_hdf[moy_0d]
                        extracted = extract_average_values(hdfMoy, r_gaz, cp)
                        for var, value in extracted.items():
                            results.append({
                                "BSAM_Name": grid_name_bsam,
                                "Omega": grid_omega,
                                "Plane_Name": plane_name,
                                "Flow": grid_flow_name,
                                "Variable": var,
                                "Value": value,
                                "gamma": gamma,
                                "r_gaz": r_gaz,
                                "cp": cp,
                            })
                        break

    return results

def load_hdf_data(cas) -> pd.DataFrame:
    data = []
    with h5py.File(cas.file_path, 'r') as f:
        for grid_name in f:
            if grid_name in ["CGNSLibraryVersion", "DataNozzle"]:
                continue
            grid = f[grid_name]
            data.extend(process_grid(grid, grid_name))

    df = pd.DataFrame(data)

    row_list = df["BSAM_Name"].dropna().unique().tolist()
    df_filtered = df[df['Plane_Name'].isin(['Inlet', 'Outlet'])]
    df_filtered["BSAM_Name"] = df_filtered["BSAM_Name"].apply(rename_row)

    return df_filtered

def load_bdd_data(cas, pair_row):
    rp = RowPair.objects.get(cas=cas, name=pair_row)

    data = {
        "Qcorr_ref": rp.Qcorr_ref,
        "Pi": rp.Pi,
        "Qcorr": rp.Qcorr,
        "Tau": rp.Tau,
        "Cd": rp.Cd,
        "Etapol": rp.Etapol,
        "KD": cas.iso_vitesse.recalage_kd,
        "PisQcorr_ref": (
            rp.Pi / rp.Qcorr_ref
            if (rp.Pi is not None and rp.Qcorr_ref not in (0, None))
            else None
        )
    }

    return data, rp

def get_value_from_df_hdf(df, name, plane, variable):
    value = df[
        (df['BSAM_Name'] == name) &
        (df['Plane_Name'] == plane) &
        (df['Variable'] == variable)
        ]['Value'].values

    return value[0]

def set_type_of_rowpair(rowpair, sheet_name):
    if sheet_name == 'Global':
        rowpair.type = 'global'
    elif re.search(r'RM\d+-RD\d+', rowpair.name):
        rowpair.type = 'etage'
    elif re.search(r'RD\d+-RM\d+', rowpair.name):
        rowpair.type = 'pseudo_etage'
    else:
        rowpair.type = 'isole'
    rowpair.save()

def add_cas_info(df, cas_inner):

    # Enrichissement pour affichage
    df["element_color"] = cas_inner.iso_vitesse.color
    df["group"] = cas_inner.iso_vitesse.name
    df["name"] = cas_inner.name
    df["id"] = cas_inner.id
    df["selected"] = cas_inner.select
    df["marker"] = cas_inner.iso_vitesse.marker
    df["fill_alpha"] = df["selected"].apply(lambda x: 8 if x else 1)
    df["line_width"] = df["selected"].apply(lambda x: 8 if x else 1)

    return df

def get_row_from_bsam(bsam):

    tf = ThroughFlow.from_bsam(bsam.file_path)

    for zone in tf.zones:
        for index, row in enumerate(zone.rows):
            row_obj, _ = Row.objects.get_or_create(
                flux=get_flux_alias(row.inlet.jflux, data_type='bsam'),
                position=index + 1,
                omega=row.omega,
                nb_blade=row.z,
                bsam_name=row.name,
                name=rename_row(row.name),
                cas=bsam,
            )

            row_obj.type = 'rotor' if row_obj.omega == 0.0 else 'stator'
            row_obj.save()

    return Row.objects.filter(cas=bsam)

def get_row_from_antares_card(case_obj):

    antarescard_filepath = os.path.join(case_obj.repertory, "calculation/carte_antares.py")

    config_dico = read_input_file(antarescard_filepath)

    for grid_key, grid_val in config_dico['gridFields'].items():
        row_obj, _ = Row.objects.get_or_create(
            flux=get_flux_alias(grid_val['Flux'], data_type='cfd'),
            position=grid_val['FluxIndex'],
            omega=grid_val['Omega'],
            nb_blade=grid_val['TotalBladeCount'],
            bsam_name=grid_val['GridBSAMName'],
            name=rename_row(grid_val['GridBSAMName']),
            cas=case_obj,
        )

        row_obj.type = 'rotor' if row_obj.omega == 0.0 else 'stator'
        row_obj.save()

    return Row.objects.filter(cas=case_obj)

def get_iso_config(iso_vitesse):

    if iso_vitesse.get_lst_row_config():
        return iso_vitesse.get_lst_row_config()

    else:
        for case in Cas.objects.filter(iso_vitesse=iso_vitesse):

            antares_file = os.path.join(
                case.repertory,
                "calculation/carte_antares.py",
            )

            config_dico = read_input_file(antares_file)
            row_data = {}
            for grid_key, grid_val in config_dico['gridFields'].items():
                row_data[grid_key] = {
                    "flux": get_flux_alias(grid_val['Flux'], data_type='cfd'),
                    "position": grid_val['FluxIndex'],
                    "omega": grid_val['Omega'],
                    "nb_blade": grid_val['TotalBladeCount'],
                    "bsam_name": grid_val['GridBSAMName']
                }

            case.row_metadata = row_data
            case.save()

        row_list_anna = get_row_from_antarescard(antares_file)
        iso_vitesse.row_config = define_config_list(row_list_anna, rename=True)
        iso_vitesse.save(update_fields=["row_config"])
        return iso_vitesse.get_lst_row_config()

def make_json_serializable(obj):
    if isinstance(obj, (np.integer, np.floating)):
        return obj.item()
    elif isinstance(obj, (datetime,)):
        return obj.isoformat()
    elif hasattr(obj, '__dict__'):
        return str(obj)  # fallback
    return obj

def find_key_in_data(data, key_to_search):

    if isinstance(data, dict):
        for key in data:
            if key == key_to_search:
                if key_to_search in data:
                    return data[key_to_search]

        for value in data.values():
            results = find_key_in_data(value, key_to_search)
            if results is not None:
                return results

    elif isinstance(data, (list, tuple, set)):
        for element in data:
            resultat = find_key_in_data(element, key_to_search)
            if resultat is not None:
                return resultat

    elif isinstance(data, pd.DataFrame):
        if key_to_search in data.columns:
            return data[key_to_search].values[0]

    return None

def get_sheet_name_from_rowpair(file_path, rowpair_obj):

    df = pd.read_excel(file_path, sheet_name=None)

    pair_row_name_split = rowpair_obj.name.split("-")

    if len(pair_row_name_split) == 1:
        row_amont, row_aval = pair_row_name_split[0], pair_row_name_split[0]
    else:
        row_amont, row_aval = pair_row_name_split[0], pair_row_name_split[1]

    for sheet in df.keys():
        upstream_plane = df[sheet].get('plan_amont')
        downstream_plane = df[sheet].get('plan_aval')
        row_name_up, row_name_down = "", ""
        if upstream_plane is not None:
            row_name_up = rename_row(upstream_plane.iloc[0].split('_')[0])
        if downstream_plane is not None:
            row_name_down = rename_row(downstream_plane.iloc[0].split('_')[0])

        print(row_name_up, row_name_down)
        if row_name_up == row_amont and row_name_down == row_aval:
            return sheet