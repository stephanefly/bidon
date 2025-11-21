import os, re, time
from bsamreader import ThroughFlow
import h5py
import pandas as pd
from typing import Dict, List
from pathlib import Path

# case_path = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_BIFLUX_IG_TO_OS"
# case_path = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_STD4_v3j_i3_R1HB_Nn_LF_27072018_1000"
# case_path = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_TS32_RM2_RD2"
case_path = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_PAT_RM1_TO_RD11"


# antarescard_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_STD4_v3j_i3_R1HB_Nn_LF_27072018_1000\calculation\carte_antares.py"
# antarescard_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_PAT_RM1_TO_RD11\calculation\carte_antares.py"
# antarescard_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_TS30_RDE_RM1_RD1_360DEG\calculation\carte_antares.py"
# antarescard_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_TS32_RM2_RD2\calculation\carte_antares.py"
# antarescard_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_BIFLUX_IG_TO_OS\calculation\carte_antares.py"

# bsam_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\Bsam\COMPACT_8etages.bsam"
# bsam_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_BIFLUX_IG_TO_OS\init\bc_BSAM"

# gradienthdf_filepath = r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\CasCannelle\case_BIFLUX_IG_TO_OS\post\postAnNA\Gradients_Complets.trac"

def timeit(func, tol=10 ** -3):
    def timed(*args, **kw):


        time_begin = time.time()
        result = func(*args, **kw)
        time_end = time.time()

        delta_time = time_end - time_begin

        return result

    return timed

def set_filepath(case_path):
    case_path = Path(case_path)
    antarescard_filepath = case_path  / "calculation/carte_antares.py"
    gradienthdf_filepath = case_path  / "post/postAnNA/Gradients_Complets.trac"
    bsam_filepath = case_path  / "init/bc_BSAM"
    perfos0d_filepath = case_path  / "post/postAnNA/Perfos0D_moy_7.xlsx"

    return antarescard_filepath, gradienthdf_filepath, bsam_filepath, perfos0d_filepath

# @timeit
def extract_average_values(hdfMoy) -> Dict[str, float]:
    extracted = {}
    for var in ["Pta", "Tta", "Q", "Ps", "Ptr"]:
        if var in hdfMoy:
            extracted[var] = hdfMoy[var][()][0]
    return extracted

@timeit
def process_grid(grid, grid_name: str) -> List[Dict]:
    results = []

    grid_name_bsam = str(grid["BSAM_NAME"][()].decode())
    grid_omega = grid["Omega"][()]
    r_gaz = grid["Rgaz"][()]
    cp = grid["polynomeCoeff"][()][0]
    gamma = cp / (cp - r_gaz)

    if "BSAM_Cuts" not in grid:
        return results

    # for plane_name in grid["BSAM_Cuts"]:
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
                        extracted = extract_average_values(hdfMoy)
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

@timeit
def read_gradient_file(file_path):
    data = []
    with h5py.File(file_path, 'r') as f:
        for grid_name in f:
            if grid_name in ["CGNSLibraryVersion", "DataNozzle"]:
                continue
            grid = f[grid_name]
            data.extend(process_grid(grid, grid_name))

    df = pd.DataFrame(data)

    plane_dict = (
        df.groupby("BSAM_Name")["Plane_Name"]
        .unique()  # pour ne pas avoir de doublons
        .apply(list)  # convertir le résultat en liste
        .to_dict()  # transformer la Series en dict
    )
    row_list = df["BSAM_Name"].dropna().unique().tolist()

    return df, plane_dict, row_list

@timeit
def read_input_file(file_path):
    input_dico = {}
    if os.path.exists(file_path):
        exec(open(file_path).read(), None, input_dico)
    return input_dico

class Row:
    def __init__(self, flux, position, omega, nb_blade, bsam_name):
        self.flux = flux
        self.position = position
        self.omega = omega
        self.nb_blade = nb_blade
        self.bsam_name = bsam_name
        self.bsam_name_alias = bsam_name
        self.type = self.set_row_type(omega)

    def set_row_type(self, omega):
        row_type = 'rotor' if omega != 0.0 else 'stator'
        return row_type

def extract_numbers_letters(chain: str):
    letters = ''.join(re.findall('[a-zA-Z]', chain))
    numbers = ''.join(re.findall(r'\d+', chain))
    return letters, numbers

def get_first_rotor(rows: list[Row]=[]):
     for index, row in enumerate(rows):
         if row.type == 'rotor':
            return index, row
     return None, None


def get_first_stator(rows: list[Row]=[]):
    for index, row in enumerate(rows):
        if row.type == 'stator':
            return index, row
    return None, None

def get_flux_alias(alias: str, data_type: str='bsam'):

    if data_type.lower() == 'bsam':
        flux_aliases = {'total': 1, 'secondaire': 3, 'primaire': 2}
    else:
        flux_aliases = {'total': 1, 'secondaire': 2, 'primaire': 3}

    for key, val in flux_aliases.items():
        if alias == key:
            return val
        if alias == val:
            return key

def get_row_by_flux(rows, flux: str='total'):
    return [row for row in rows if row.flux == flux]

def rename_row(row_name: str) -> str:
    name_aliases = {
        'HDE': 'RDE',
        'BDE': 'RDE',
        'IGV': 'RDE',
        'R': 'RM',
        'S': 'RD',
        'HR': 'RM',
        'HS': 'RD',
        'BR': 'RM',
        'BS': 'RD',
        'OG': 'OGV',
    }

    row_basename, row_number = extract_numbers_letters(row_name)
    row_basename_new = name_aliases.get(row_basename, row_basename)

    return row_basename_new + row_number

def find_row_by_renamed_bsam(row_dict, target_name):
    for row_key, values in row_dict.items():
        bsam_name = values["bsam_name"]
        renamed = rename_row(bsam_name)
        if renamed == target_name:
            return {row_key: values}
    return None


def define_config_list(rows: list[Row]=[], rename: bool=True):

    config_list = {'global': [], 'etage': [], 'pseudo_etage': [], 'isole': []}
    for flux in ['total', 'secondaire', 'primaire']:
        rows_by_flux = get_row_by_flux(rows, flux)

        first_rotor_index, first_rotor = get_first_rotor(rows_by_flux)
        first_stator_index, first_stator = get_first_stator(rows_by_flux)

        nb_row = len(rows_by_flux)

        if rename:
            for row in rows_by_flux:
                row.bsam_name_alias = rename_row(row.bsam_name)

        if len(rows_by_flux) > 1:
            config_list['global'].append(f'{rows_by_flux[0].bsam_name_alias}-{rows_by_flux[-1].bsam_name_alias}')

        if first_rotor_index is not None:
            for index in range(first_rotor_index, nb_row, 2):
                index_begin = index
                index_end = index_begin + 1
                if index_begin < len(rows_by_flux) and index_end < len(rows_by_flux):
                    _, stage_nb = extract_numbers_letters(rows_by_flux[index_begin].bsam_name_alias)
                    label = f"{rows_by_flux[index_begin].bsam_name_alias}-{rows_by_flux[index_end].bsam_name_alias}"
                    if label not in config_list['global']: # pour eviter les doublons
                        config_list['etage'].append(label)

        if first_stator_index is not None:
            for index in range(first_stator_index, nb_row - 1, 2):
                index_begin = index
                index_end = index_begin + 1
                if index_begin < len(rows_by_flux) and index_end < len(rows_by_flux):
                    _, pseudo_nb = extract_numbers_letters(rows_by_flux[index_end].bsam_name_alias)
                    label = f"{rows_by_flux[index_begin].bsam_name_alias}-{rows_by_flux[index_end].bsam_name_alias}"
                    if label not in config_list['global']:  # pour eviter les doublons
                        config_list['pseudo_etage'].append(label)

        config_list['isole'].extend([row.bsam_name_alias for row in rows_by_flux])

    return config_list

def get_row_from_antarescard(file_path):

    config_dico = read_input_file(file_path)

    row_list = []
    for grid in config_dico['gridFields']:

        row_list.append(Row(
            flux=get_flux_alias(config_dico['gridFields'][grid]['Flux'], data_type='cfd'),
            position=config_dico['gridFields'][grid]['FluxIndex'],
            omega=config_dico['gridFields'][grid]['Omega'],
            nb_blade=config_dico['gridFields'][grid]['TotalBladeCount'],
            bsam_name=config_dico['gridFields'][grid]['GridBSAMName']
        ))
    return row_list

def get_row_from_bsam(file_path):

    tf = ThroughFlow.from_bsam(file_path)

    row_list = []
    for zone in tf.zones:
        for index, row in enumerate(zone.rows):
            row_list.append(Row(
                flux=get_flux_alias(row.inlet.jflux, data_type='bsam'),
                position=index + 1,
                omega=row.omega,
                nb_blade=row.z,
                bsam_name=row.name
            ))
    return row_list

@timeit
def read_excel_file(file_path, rename: bool=True):

    df = pd.read_excel(file_path, sheet_name=None)

    config = {'global': [], 'etage': [], 'pseudo_etage': [], 'isole': []}

    for sheet in df.keys():
        upstream_plane = df[sheet].get('plan_amont')
        downstream_plane = df[sheet].get('plan_aval')

        if upstream_plane is not None:
            row_name_up = upstream_plane.iloc[0].split('_')[0]
            if rename:
                row_name_up = rename_row(row_name_up)
        if downstream_plane is not None:
            row_name_down = downstream_plane.iloc[0].split('_')[0]
            if rename:
                row_name_down = rename_row(row_name_down)

        if upstream_plane is not None and downstream_plane is not None:
            if 'global' in sheet.lower():
                if row_name_up != row_name_down:
                    config['global'].append(f"{row_name_up}-{row_name_down}")
            elif 'pseudo_etage' in sheet.lower():
                config['pseudo_etage'].append(f"{row_name_up}-{row_name_down}")
            elif 'etage' in sheet.lower():
                config['etage'].append(f"{row_name_up}-{row_name_down}")
            else:
                config['isole'].append(f"{row_name_up}")

    return df , config

if __name__ == "__main__":


    antarescard_filepath, gradienthdf_filepath, bsam_filepath, perfos0d_filepath = set_filepath(case_path)
    rename = True

    # if os.path.exists(perfos0d_filepath):
    #     print(f"\nLECTURE FICHIER EXCEL --> {perfos0d_filepath}")
    #     df, config_excel = read_excel_file(perfos0d_filepath, rename=rename)
    #
    #     print(f"    * CONFIG EXCEL = {config_excel}")
    #
    # if os.path.exists(gradienthdf_filepath):
    #     print(f"\nLECTURE GRADIENT HDF --> {gradienthdf_filepath}")
    #     df, plane_dict, row_list = read_gradient_file(gradienthdf_filepath)
    #     if rename:
    #         row_list = [rename_row(row) for row in row_list]
    #     else:
    #         row_list = [row for row in row_list]
    #     print(f"    * row_list = {row_list}")
    #
    #
    # if os.path.exists(antarescard_filepath):
    #     row_list_anna = get_row_from_antarescard(antarescard_filepath)
    #
    #
    #
    #     # for row in row_list_anna:
    #     #     print(f"     * {row.bsam_name} --> type = {row.type}, flux={row.flux}, position={row.position}, omega={row.omega}, nb_blade={row.nb_blade}")
    #
    #     config = define_config_list(row_list_anna, rename=rename)
    #
    if os.path.exists(bsam_filepath):
        print(f"\nLECTURE BSAM --> {bsam_filepath}")
        row_list_bsam = get_row_from_bsam(bsam_filepath)

        # for row in row_list_bsam:
        #     print(f"{row.bsam_name} --> type = {row.type}, flux={row.flux}, position={row.position}, omega={row.omega}, nb_blade={row.nb_blade}")

        config = define_config_list(row_list_bsam, rename=rename)
        print(f"    * CONFIG BSAM= {config}")