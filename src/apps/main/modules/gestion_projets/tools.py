import shutil
import os
import subprocess


from pathlib import Path

import yaml
from pylnk3 import for_file

from django.conf import settings
from pylnk3 import Lnk
from apps.main.models import UtilitaireConfiguration
from config.settings.base import PATH_STYLE


def get_color_list():
    return {
        # Couleurs brutes (vives, bien reconnaissables)
        "#000000": {"fr": "Noir", "en": "Black"},
        "#FF4136": {"fr": "Rouge", "en": "Red"},
        "#0074D9": {"fr": "Bleu", "en": "Blue"},
        "#2ECC40": {"fr": "Vert", "en": "Green"},
        "#B10DC9": {"fr": "Violet", "en": "Violet"},
        "#FF851B": {"fr": "Orange", "en": "Orange"},
        "#FFDC00": {"fr": "Jaune", "en": "Yellow"},
        "#de00bc": {"fr": "Rose", "en": "Pink"},
        "#8B4513": {"fr": "Marron", "en": "Brown"},
        "#7F8C8D": {"fr": "Gris", "en": "Grey"},
        "#850000": {"fr": "Rouge foncé", "en": "DarkRed"},
        "#ff5d5d": {"fr": "Rouge clair", "en": "LightRed"},
        "#ff7400": {"fr": "Rouge orangé", "en": "OrangeRed"},
        "#0011b2": {"fr": "Bleu foncé", "en": "DarkBlue"},
        "#002eff": {"fr": "Bleu royal", "en": "RoyalBlue"},
        "#29b6f6": {"fr": "Bleu clair", "en": "LightBlue"},
        "#71ff7c": {"fr": "Vert clair", "en": "LightGreen"},
        "#007509": {"fr": "Vert foncé", "en": "DarkGreen"},
    }


def get_color_name_from_code(color_code, lang="fr"):
    color_dict = get_color_list()
    return color_dict.get(color_code, {}).get(lang)


def get_color_code_from_name(color_name_fr):
    for code, names in get_color_list().items():
        if names.get("fr") == color_name_fr:
            return code
    return None


def get_color_en_from_fr_name(color_name_fr):
    color_code = get_color_code_from_name(color_name_fr)
    if color_code:
        return get_color_name_from_code(color_code, lang="en")
    return None


def get_symbol_list():
    return {
        "circle": {
            "fr": "Cercle ●",
            "value": "circle",
            "symbol": "●",
            "mpl": "o"           # cercle
        },
        "square": {
            "fr": "Carré ■",
            "value": "square",
            "symbol": "■",
            "mpl": "s"           # carré
        },
        "triangle": {
            "fr": "Triangle Haut ▲",
            "value": "triangle",
            "symbol": "▲",
            "mpl": "^"           # triangle vers le haut
        },
        "inverted_triangle": {
            "fr": "Triangle Bas ▼",
            "value": "inverted_triangle",
            "symbol": "▼",
            "mpl": "v"           # triangle vers le bas
        },
        "x": {
            "fr": "Croix ✕",
            "value": "x",
            "symbol": "✕",
            "mpl": "x"           # croix diagonale
        },
        "cross": {
            "fr": "Plus ✚",
            "value": "cross",
            "symbol": "✚",
            "mpl": "+"           # croix classique
        },
        "asterisk": {
            "fr": "Étoile ✱",
            "value": "asterisk",
            "symbol": "✱",
            "mpl": "*"           # étoile
        },
        "hex": {
            "fr": "Hexagone ⬡",
            "value": "hex",
            "symbol": "⬡",
            "mpl": "h"           # hexagone
        }
    }


def get_symbol_name_from_code(symbol_code):
    symbol_dict = get_symbol_list()
    return symbol_dict.get(symbol_code, {}).get("mpl")


def move_genepi_file(obj):
    base_dir = Path(settings.BASE_DIR)

    # Création du dossier GenepiAuto si inexistant
    work_dir = Path(obj.work_directory)
    dst_dir = work_dir / "GenepiAuto"
    dst_dir.mkdir(parents=True, exist_ok=True)

    # --- Source dico ---
    if getattr(obj, "dico_genepi_auto", None):
        src_dico = Path(obj.dico_genepi_auto)

        # Si c'est un chemin relatif, on le rattache à BASE_DIR
        if not src_dico.is_absolute():
            src_dico = base_dir / src_dico
    else:
        src_dico = base_dir / "apps" / "main" / "modules" / "genepi" / "FILES" / "GENEPIAuto_Dico_Default.py"

    # --- Dest dico ---
    dst_dico = work_dir / "GenepiAuto" / src_dico.name
    shutil.copy2(str(src_dico), str(dst_dico))

    # Option : mettre à jour le champ pour pointer vers le fichier copié (sans save ici)
    if hasattr(obj, "dico_genepi_auto"):
        obj.dico_genepi_auto = str(dst_dico)

    # --- Copier genepi ---
    src_genepi = base_dir / "apps" / "main" / "modules" / "genepi" / "FILES" / "genepi_auto.py"
    dst_genepi = work_dir / "GenepiAuto" / src_genepi.name
    shutil.copy2(str(src_genepi), str(dst_genepi))

    os.chmod(dst_genepi, 0o777)
    os.chmod(dst_dico, 0o777)

    return dst_genepi, dst_dico


def copy_dirs_only(src: Path, dst: Path):
    src = Path(src)
    dst = Path(dst)

    for root, dirs, _ in os.walk(src):
        root = Path(root)
        relative_path = root.relative_to(src)
        target_dir = dst / relative_path

        target_dir.mkdir(parents=True, exist_ok=True)


def load_carac_config(
    nb_graph,
        filepath=Path(settings.BASE_DIR) / "apps" / "main" / "modules" / "bsam" / "carac_config.yaml",
):
    with open(filepath, encoding="utf-8") as file:
        config = yaml.safe_load(file)
    for carac in config.get("lst_carac", []):
        if not carac.get("Nb_hauteur_base"):
            carac["Nb_hauteur_base"] = nb_graph
    return config.get("lst_carac", [])

def create_bat_shortcut_windows(model, user):

    genepi_path = UtilitaireConfiguration.objects.get(user=user).genepi_path

    # Ton batch existant
    batch_file = Path(os.path.join(genepi_path, "GENEPIbatch.bat")) # adapter si besoin

    # Où déposer le .lnk
    path_lnk = Path(model.work_directory) / "GenepiAuto" / "GENEPIbatch.lnk"

    # Commande PowerShell pour créer le raccourci
    ps_command = f'''
    $WshShell = New-Object -ComObject WScript.Shell;
    $Shortcut = $WshShell.CreateShortcut("{path_lnk}");
    $Shortcut.TargetPath = "{batch_file}";
    $Shortcut.WorkingDirectory = "{batch_file.parent}";
    $Shortcut.IconLocation = "C:\\Windows\\System32\\cmd.exe,0";
    $Shortcut.Save();
    '''

    subprocess.run(["powershell", "-Command", ps_command], check=True)


def create_bat_shortcut_linux(model, user):
    genepi_path = UtilitaireConfiguration.objects.get(user=user).genepi_path
    content = f"{genepi_path}\GENEPIbatch.bat %1"

    workdir = Path(model.work_directory)
    workdir.mkdir(parents=True, exist_ok=True)

    genepi_dir = workdir / "GenepiAuto"
    os.chmod(genepi_dir, 0o777)

    bat_path = workdir / "GenepiAuto" / "GENEPIbatch.bat"

    with open(bat_path, "w", encoding="cp1252", newline="\r\n") as f:
        f.write(content + "\r\n")
        f.write("pause\r\n")

    # Permissions Linux : lecture + écriture pour tous
    os.chmod(bat_path, 0o777)

    return bat_path


def move_cannelle_auto_file(obj):
    base_dir = Path(settings.BASE_DIR)

    # Création du dossier GenepiAuto si inexistant
    work_dir = Path(obj.work_directory)
    dst_dir = work_dir
    dst_dir.mkdir(parents=True, exist_ok=True)

    # --- Source dico ---
    src_dico = base_dir / "apps" / "main" / "modules" / "genepi" / "FILES" / "CannelleAuto_Main.py"

    # --- Dest dico ---
    dst_dico = work_dir / src_dico.name
    shutil.copy2(str(src_dico), str(dst_dico))

    os.chmod(dst_dico, 0o777)

    return dst_dico

def create_cannelle_bat_shortcut_windows(model, user):

    cannelle_path = UtilitaireConfiguration.objects.get(user=user).cannelle_path

    # Ton batch existant
    batch_file = Path(os.path.join(cannelle_path, "cannelle_batch.bat")) # adapter si besoin

    # Où déposer le .lnk
    path_lnk = Path(model.work_directory) / "CannelleAuto_Launcher.lnk"

    # Commande PowerShell pour créer le raccourci
    ps_command = f'''
    $WshShell = New-Object -ComObject WScript.Shell;
    $Shortcut = $WshShell.CreateShortcut("{path_lnk}");
    $Shortcut.TargetPath = "{batch_file}";
    $Shortcut.WorkingDirectory = "{batch_file.parent}";
    $Shortcut.IconLocation = "C:\\Windows\\System32\\cmd.exe,0";
    $Shortcut.Save();
    '''

    subprocess.run(["powershell", "-Command", ps_command], check=True)


def create_cannelle_bat_shortcut_linux(model, user):
    genepi_path = UtilitaireConfiguration.objects.get(user=user).genepi_path
    content = f"{genepi_path}\cannelle_batch.bat %1"

    workdir = Path(model.work_directory)
    workdir.mkdir(parents=True, exist_ok=True)

    bat_path = workdir / "cannelle_batch.bat"

    with open(bat_path, "w", encoding="cp1252", newline="\r\n") as f:
        f.write(content + "\r\n")
        f.write("pause\r\n")

    # Permissions Linux : lecture + écriture pour tous
    os.chmod(bat_path, 0o777)

    return bat_path