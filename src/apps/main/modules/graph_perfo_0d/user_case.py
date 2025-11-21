from apps.main.models import Cas, Etat, IsoVitesse, Row, RowPair
import os, uuid, pathlib
import pandas as pd
from django.http import request
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
import pandas as pd
from collections import defaultdict
import re
from apps.main.modules.graph_perfo_0d.gestion_data import set_inlet_outlet_row_obj

def lecture_user_file_curve(f, iso_vitesse):
    # Lecture de fichier

    ext = pathlib.Path(f.name).suffix.lower()
    # Nom unique
    ts = timezone.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{ts}_{uuid.uuid4().hex}{ext}"
    # Sauvegarde physique
    fs = FileSystemStorage(
        location=os.path.splitext(iso_vitesse.etat.get_cache_filepath())[0])

    saved_name = fs.save(filename, f)
    file_path = fs.path(saved_name)
    # Lecture 1er onglet
    df = pd.read_excel(file_path, sheet_name=0, engine="xlrd")

    return df, file_path

def _base_name(col: str) -> str:
    # "GLOBAL RDE-OGV.2" -> "GLOBAL RDE-OGV"
    return col.split('.')[0].strip()

def _build_schema(df: pd.DataFrame):
    """
    La ligne 0 contient les sous-clés (Qcorr_ref, etapol, Pi, Tau, …).
    Construit { base_col : [(colname, subkey), …] }.
    """
    schema = defaultdict(list)
    for col in df.columns[1:]:  # 1ère colonne = point
        base = _base_name(col)
        subkey = str(df.loc[0, col]).strip()
        if subkey == "" or subkey.lower() == "nan":
            subkey = f"var_{len(schema[base])}"
        schema[base].append((col, subkey))
    return dict(schema)

def dico_listes_par_colonne(df: pd.DataFrame, iso_vitesse, file_path) :
    """
    Retourne:
    {
      "RDE-OGV": [ {"point": 1393, "Qcorr_ref": …, "etapol": …, "Pi": …, "Tau": …}, {...}, ... ],
      "RDE-RM1": [ {...}, ... ],
      "RDE-RM3": [ {...}, ... ],
      ...
    }
    Hypothèse: la ligne 0 du DataFrame porte les sous-en-têtes.
    """
    point_col = df.columns[0]
    schema = _build_schema(df)

    out = {base: [] for base in schema.keys()}
    # Parcourt toutes les lignes de données (à partir de 1)
    for row in range(1, len(df)):
        point_val = df.loc[row, point_col]
        print(point_val)
        point_cas = Cas.objects.create(
            name=point_val,
            iso_vitesse=iso_vitesse,
            file_path=file_path,
        )
        point_cas.obj_type = "cas_utilisateur"
        point_cas.save()
        for base, items in schema.items():
            entry = {"point": point_val}
            for col, subkey in items:
                entry[subkey] = df.loc[row, col]
            out[base].append(entry)
    return out


def build_config_row(data: dict):
    result = {"global": [], "etage": [], "pseudo_etage": [], "isole": []}

    for i, key in enumerate(data.keys()):
        if i == 0 :
            result["global"].append(key)
        elif key.startswith("RM") and "-" in key:
            result["etage"].append(key)
        elif key.startswith("RD") and "-" in key:
            result["pseudo_etage"].append(key)
        elif "-" not in key:
            result["isole"].append(key)

    print(result)
    return result



def build_row_list(structure: dict):
    unique_parts = set()
    for group in structure.values():
        for elt in group:
            unique_parts.update(elt.split('-'))

    row_list = sorted(unique_parts)  # trié, optionnel
    print(row_list)

    return row_list


def save_to_database(lst_row, data_file, iso_vitesse):
    lst_cas_obj = Cas.objects.filter(iso_vitesse=iso_vitesse)
    for row_index, row in enumerate(lst_row):
        for cas in lst_cas_obj:
            row_obj, _ = Row.objects.get_or_create(
                flux='total',
                name=row,
                bsam_name=row,
                cas=cas,
                position=row_index + 1,
            )
            if 'RM' in row:
                row_obj.type = 'rotor'
            else:
                row_obj.type = 'stator'
            row_obj.save()
    for key, lst_cas_value in data_file.items():
        for cas_value in lst_cas_value:
            case_obj = Cas.objects.get(
                name=cas_value["point"], iso_vitesse=iso_vitesse)

            rowpair_obj, _ = RowPair.objects.get_or_create(
                name=key,
                cas=case_obj,
            )
            rowpair_obj.Qcorr_ref = float(cas_value["Qcorr_ref"])

            try:
                rowpair_obj.Pi = float(cas_value["Pi"])
                rowpair_obj.calculate_pis_qcorr_ref()
            except:
                pass
            try:
                rowpair_obj.calculate_Qcorr(cas_value["Tau"])
            except:
                pass
            try:
                rowpair_obj.Etapol = float(cas_value["etapol"])
            except:
                pass
            try:
                rowpair_obj.Tau = float(cas_value["Tau"])
            except:
                pass
            try:
                rowpair_obj.Cd = float(cas_value["Cd"])
            except:
                pass
            rowpair_obj.save()

            set_inlet_outlet_row_obj(case_obj, rowpair_obj)