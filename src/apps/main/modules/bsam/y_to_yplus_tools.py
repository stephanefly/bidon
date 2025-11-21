import os
import datetime
from pathlib import Path
from django.conf import settings


def copy_bsam_file(bsam_path: str, work_dir: Path) -> Path:
    """Copie le fichier BSAM dans le répertoire de travail"""
    bsam_path = bsam_path.replace('"', '').strip()
    dest_bsam = work_dir / os.path.basename(bsam_path)

    if os.path.isfile(bsam_path):
        with open(bsam_path, "rb") as fsrc, open(dest_bsam, "wb") as fdst:
            fdst.write(fsrc.read())

    return dest_bsam


def create_launch_bat(work_dir: Path):
    """Crée un fichier batch pour exécuter compute_wallcellsize.py"""
    bat_content = r"""@echo off
color 71
rem #######################################
rem #
rem #   CANNELLE application launching script
rem #
rem #   STILOG IST 2024
rem #
rem ######################################

set CNL_HOME=%~dp0
call %CNL_HOME%\setenv.bat

cd /d %CNL_HOME%

for /f %%d in ('%PYTHON_EXE% -m pipenv --venv') do set VENVDIR=%%d
echo Localisation de l'environnement virtuel: %VENVDIR%

if "%VENVDIR%"=="" (
     %PYTHON_EXE% -m pipenv --python %PYTHON_EXE%
     for /f %%d in ('%PYTHON_EXE% -m pipenv --venv') do set VENVDIR=%%d
)

set VENV_PYEXE=%VENVDIR%\Scripts\python.exe
%PYTHON_EXE% -m pipenv run pip install -r requirements.txt | findstr /V /C:"already satisfied"

%VENV_PYEXE% compute_wallcellsize.py

rem pause
"""
    (work_dir / "launch_cannelle.bat").write_text(bat_content, encoding="utf-8")


def _script_header(dest_bsam: Path, y_value):
    return f"""# -------------------------------------------------------------------------------------
# Script généré automatiquement
# -------------------------------------------------------------------------------------

bsam_filepath = [r"{dest_bsam}"]

yplus_target = {y_value}

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

import scipy
import numpy as np
import lec_bsam.readBSAM as readBSAM
from scipy import optimize
from numpy.polynomial import Polynomial
from pathlib import Path
"""


def _script_core() -> str:
    return """def get_info_from_grid(res_goux, igrid):
    if res_goux.BIFLUX:
        if (igrid < res_goux.NGRID[0]):
            iflux = 0
            jam = res_goux.noms_grille[igrid].jam - 1
            jav = res_goux.noms_grille[igrid].jav - 1
            lci = res_goux.fluxList[iflux].planList[jam].LCI - 1
            lce = res_goux.fluxList[iflux].planList[jam].LCE - 1
        elif (res_goux.NGRID[0] <= igrid and igrid < res_goux.NGRID[0] + res_goux.NGRID[1]):
            iflux = 1
            jam = res_goux.noms_grille[igrid].jam - res_goux.NPL[0] - 1
            jav = res_goux.noms_grille[igrid].jav - res_goux.NPL[0] - 1
            lci = res_goux.fluxList[iflux].planList[jam].LCI - 1
            lce = res_goux.fluxList[iflux].planList[jam].LCE - 1
        else:
            iflux = 2
            jam = res_goux.noms_grille[igrid].jam - res_goux.NPL[0] - 1
            jav = res_goux.noms_grille[igrid].jav - res_goux.NPL[0] - 1
            lci = res_goux.fluxList[iflux].planList[jam].LCI - res_goux.NLG[1] - 1
            lce = res_goux.fluxList[iflux].planList[jam].LCE - res_goux.NLG[1] - 1
    else:
        iflux = 0
        jam = res_goux.noms_grille[igrid].jam - 1
        jav = res_goux.noms_grille[igrid].jav - 1
        lci = res_goux.fluxList[iflux].planList[jam].LCI - 1
        lce = res_goux.fluxList[iflux].planList[jam].LCE - 1

    return iflux, jam, jav, lci, lce


def compute_wallcellsize(bsam_filepath, yplus_target=1):
    def func(x, rey, beta=2.51):
        return 1. / np.sqrt(x) + 2. * np.log10(beta / rey / np.sqrt(x))

    def compute_utau_u(x):
        return np.sqrt(x / 8.)

    def compute_cf(utau_u):
        return 2. * np.power(utau_u, 2.)

    def mu(t, tref=273.15, ta=110.4):
        return 1.711 * 1.e-5 * np.power(t / tref, 1.5) * (tref + ta) / (t + ta)

    def rho(t, p, mair=0.0289644, r=8.3144621):
        return p * mair / r / t

    res_goux = readBSAM.lecGoux(bsam_filepath)

    print("\\n\\n==============================================================================")
    print(f" Estimation de la taille de premiere maille pour un y+ cible={yplus_target}:")
    print(f"  --> Bsam path: {bsam_filepath}")
    print("==============================================================================")

    for igrid in range(res_goux.NGRID[3]):
        # ... ici tout ton code de calcul ...
        pass

    return 0


if __name__ == "__main__":
    for bsam_file in bsam_filepath:
        file_path = Path(bsam_file)
        if file_path.exists():
            compute_wallcellsize(bsam_file, yplus_target)
        else:
            print("\\n\\n==============================================================================")
            print(f" /!/!/! Le Bsam suivant n'existe pas: {file_path}")
            print("==============================================================================")
"""


def create_python_script(dest_bsam: Path, work_dir: Path, y_value):
    """Assemble et écrit le script Python"""
    py_content = _script_header(dest_bsam, y_value) + _script_core()
    (work_dir / "compute_wallcellsize.py").write_text(py_content, encoding="utf-8")


def create_repertory_y_yplus(bsam_path: str, username: str, y_value, fichier):
    """Pipeline principal : crée le dossier, copie le bsam, génère .bat et .py"""

    # 1. Créer répertoire daté
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    work_dir = Path(settings.WORKING_REPERTORY) / username / "y_to_y+" / date_str
    work_dir.mkdir(parents=True, exist_ok=True)

    # 2. Sauvegarder le fichier
    file_path = work_dir / fichier.name
    with open(file_path, "wb+") as destination:
        for chunk in fichier.chunks():
            destination.write(chunk)

    # 2. Copier le BSAM
    dest_bsam = copy_bsam_file(bsam_path, work_dir)

    # 3. Créer .bat
    create_launch_bat(work_dir)

    # 4. Créer script Python
    create_python_script(file_path, work_dir, y_value)

    # 5. Retourner chemins utiles
    result_path = str(work_dir)
    parts = work_dir.parts
    result_path_display = str(Path(*parts[-3:]))

    return result_path, result_path_display
