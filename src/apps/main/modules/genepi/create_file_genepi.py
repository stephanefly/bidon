import os
import pprint

from apps.main.models import UtilitaireConfiguration
from apps.main.modules.gestion_projets.tools import (get_color_name_from_code,
                                                     get_color_en_from_fr_name,
                                                     get_symbol_name_from_code)
from django.conf import settings


def create_genepi_file(etat, lst_cas_selected, param_genepi):
    genepi_file = os.path.join(
        etat.work_directory,
        'GenepiAuto',
        "GENEPIAuto_" + str(param_genepi["titre"]) + "_Main.py"
    )

    contenu = complete_genepi_file(param_genepi)

    cas_cannelle_list = [obj for obj in lst_cas_selected if
                         obj.obj_type == "cas_cannelle"]
    bsam_list = [obj for obj in lst_cas_selected if
                         obj.obj_type == "bsam"]

    lines_cas = create_info_cas_lines(cas_cannelle_list, param_genepi)
    lines_bsam = create_info_bsam_lines(bsam_list, param_genepi)


    with open(genepi_file, "w", encoding="utf-8") as fichier:
        fichier.write("\n".join(lines_cas))
        fichier.write("\n".join(lines_bsam))
        fichier.write(contenu)


def create_info_cas_lines(lst_cas_selected, param_genepi):
    lines = []

    line_type = 10 * ['SolidLine', 'DashLine', 'DotLine', 'DashDotLine', 'DashDotDotLine', 'NoPen']

    nbre_cas_par_iso = {}
    for i, cas in enumerate(lst_cas_selected, start=1):
        if i == 1:
            lines.append("# CAS CANNELLE")

        if cas.iso_vitesse.name not in nbre_cas_par_iso:
            nbre_cas_par_iso[cas.iso_vitesse.name] = 1
        else:
            nbre_cas_par_iso[cas.iso_vitesse.name] += 1

        color_anglais = get_color_name_from_code(cas.iso_vitesse.color, "en")

        lines.append(f"\nInfoCasCFD_{i} = {{}}")
        lines.append(f"InfoCasCFD_{i}['CheminBsam'] = r'{cas.bsam_path}'")
        lines.append(f"InfoCasCFD_{i}['CheminCas'] = [r'{cas.repertory}\\post']")
        if nbre_cas_par_iso[cas.iso_vitesse.name] == 1:
            lines.append(f"InfoCasCFD_{i}['TitreCas'] = '{cas.iso_vitesse.name}'")
        else:
            lines.append(f"InfoCasCFD_{i}['TitreCas'] = '{cas.iso_vitesse.name} - {nbre_cas_par_iso[cas.iso_vitesse.name]:02d}'")
        lines.append(f"InfoCasCFD_{i}['Couleur'] = '{color_anglais}'")
        lines.append(f"InfoCasCFD_{i}['DeltaCasRef'] = 'BSAM'")
        lines.append(f"InfoCasCFD_{i}['DetectionCasProcheBSAM'] = {int(param_genepi['DetectionCasProcheBSAM'])}")
        lines.append(f"InfoCasCFD_{i}['Epaisseur'] = 2")
        lines.append(f"InfoCasCFD_{i}['ImportCarmaAuto'] = 1")
        lines.append(f"InfoCasCFD_{i}['InverserBsam'] = 1")
        lines.append(f"InfoCasCFD_{i}['LiaisonCasCarma'] = ''")
        lines.append(f"InfoCasCFD_{i}['Ligne'] = '{line_type[i-1]}'")
        lines.append(f"InfoCasCFD_{i}['MisesDetectionCoupeAuto'] = 0")
        lines.append(f"InfoCasCFD_{i}['RecalageKD'] = {int(param_genepi['RecalageKD'])}")
        lines.append(f"InfoCasCFD_{i}['RetournerAubeGcolter'] = 0")
        lines.append(f"InfoCasCFD_{i}['SymboleEpaisseur'] = 4")
        lines.append(f"InfoCasCFD_{i}['SymboleIso'] = 'o'")
        lines.append(f"InfoCasCFD_{i}['TraceBSAM'] = 0")
        lines.append(f"InfoCasCFD_{i}['TrierIso'] = {int(param_genepi['TrierIso'])}")
        lines.append(f"InfoCasCFD_{i}['TypePost'] = 'ANNA'")

    lines.append("\n")

    return lines


def create_info_bsam_lines(lst_bsam_selected, param_genepi):
    lines = []

    bsam_file_path = []
    for bsam in lst_bsam_selected:
        if bsam.file_path not in bsam_file_path:
            bsam_file_path.append(bsam.file_path)
        else:
            lst_bsam_selected.remove(bsam)

    for i, bsam in enumerate(lst_bsam_selected, start=1):
        color_anglais = get_color_name_from_code(bsam.iso_vitesse.color, "en")
        if i == 1:
            lines.append("# CAS BSAM")

        symbole = get_symbol_name_from_code(bsam.iso_vitesse.marker)

        lines.append(f"\nInfoCasBSAM_{i} = {{}}")
        lines.append(f"InfoCasBSAM_{i}['CheminBsam'] = r'{bsam.file_path}'")
        lines.append(f"InfoCasBSAM_{i}['TitreCas'] = '{bsam.name}'")
        lines.append(f"InfoCasBSAM_{i}['Couleur'] = '{color_anglais}'")
        lines.append(f"InfoCasBSAM_{i}['DeltaCasRef'] = ''")
        lines.append(f"InfoCasBSAM_{i}['Epaisseur'] = 2")
        lines.append(f"InfoCasBSAM_{i}['InverserBsam'] = 1")
        lines.append(f"InfoCasBSAM_{i}['LiaisonCasCarma'] = ''")
        lines.append(f"InfoCasBSAM_{i}['Ligne'] = 'NoPen'")
        lines.append(f"InfoCasBSAM_{i}['Symbole'] = '{symbole}'")

    lines.append("\n")

    return lines


def complete_genepi_file(param_genepi):

    genepi_dico_path = os.path.dirname(os.path.normpath(param_genepi["mise_en_forme"]))
    genepi_dico_file, genepi_dico_ext = os.path.splitext(os.path.basename(os.path.normpath(param_genepi["mise_en_forme"])))
    genepiauto_filepath = os.path.join(settings.BASE_DIR, "apps", "main", "modules", "genepi", "genepi_auto.py")

    dico_str = pprint.pformat(param_genepi["dico_aubes"], width=100)

    a = rf"""#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------
# TITRE DE LA PRESENTATION

TitrePres = "{param_genepi["titre"]}"

#-------------------------------------------------------------------------------------------------------------------
# CHOIX DES EXPORT DE LA PRESENTATION

ExportPDF = {param_genepi["ExportPDF"]}
ExportExcel = {param_genepi["ExportExcel"]}
ExportPPT = {param_genepi["ExportPPT"]}

#-------------------------------------------------------------------------------------------------------------------
# AFFICHAGE OU NON DE LA LEGENDE

AfficherLegende = 0

#-------------------------------------------------------------------------------------------------------------------
# CHOIX DES POST-TRAITEMENTS A EFFECTUER

Trace_InfosCas = 1
Trace_InfosPlanUtilisateur = 1
Trace_QualiteMaillage = 0
Trace_VisuQualiteMaillage = 0
Trace_ConvDebit = 0
Trace_ConvResidus = 0
Trace_ParVariable = 0
Trace_GradientMoyAdim = 0
Trace_LoisGeom = 0
Trace_Perfos0D = 1
Trace_ProfilsRadiaux = 1
Trace_ProfilVsCorde = 1
Trace_ProfilsRadiauxAngle = 1
Trace_ProfilAzimuthaux = 1
Trace_Polaire = 0
Trace_EvolutionParois = 0
Trace_EvolutionAxiale = 0
Trace_EvolutionMeridienne = 0

#-------------------------------------------------------------------------------------------------------------------
# LISTE DES AUBES A TRACER : --> NE DOIT PAS ETRE VIDE !!!!!
DicoLabelAube2Trace = {dico_str}

#-------------------------------------------------------------------------------------------------------------------
# MODE DE PRESENTATION
ModeMises = False
ModeChamps = False

#-------------------------------------------------------------------------------------------------------------------
# RENOMMAGE DES PLANS DE POST-TRAITEMENT:

PlanCFD_AmontPerfo='Inlet'
PlanCFD_AvalPerfo='Outlet'
PlanCFD_ProcheBA='(BA)'
PlanCFD_ProcheBF='(BF)'
PlanCFD_LoinBA='Inlet'
PlanCFD_LoinBF='Outlet'

PlanBSAM_AmontPerfo='(BA)'
PlanBSAM_AvalPerfo='(BF)'
PlanBSAM_ProcheBA='(BA)'
PlanBSAM_ProcheBF='(BF)'
PlanBSAM_LoinBA='(BA-2)'
PlanBSAM_LoinBF='(BF+2)'

PlanGcolter_Amont='(BA)'
PlanGcolter_Aval='(BF)'

#-------------------------------------------------------------------------------------------------------------------
# IMPORT DES DICTIONNAIRES DE TRACE
import sys

genepi_dico_path = r'{genepi_dico_path}'
if genepi_dico_path not in sys.path:
    sys.path.append(genepi_dico_path)

from {genepi_dico_file} import *

#-------------------------------------------------------------------------------------------------------------------
# CHEMIN VERS LE SCRIPT GENEPIAUTO
exec(open(r'{genepiauto_filepath}', 'r', encoding='utf8').read(), locals())
"""
    return a


def create_genepi_bat_file(etat_work_directory, request):

    genepi_path = UtilitaireConfiguration.objects.get(user=request.user).genepi_path

    content = rf"""@echo off
setlocal

REM === CONFIGURATION DES VARIABLES D'ENVIRONNEMENT ===
set ENVIRONMENT=SAE
set ModeGENEPI=batch
set ModeGUEPARD=Serveur

set BASEDIR={genepi_path}
set ORACLE_HOME=%BASEDIR%\..\bin\win64\instantclient_11_2_64bit
set PYTHONHOME=%BASEDIR%\..\bin\win64\Python37
set PYTHONPATH=%BASEDIR%;%PYTHONHOME%;%BASEDIR%\GENEPI;%BASEDIR%\GENEPI\modules
set PATH=%PYTHONHOME%;%ORACLE_HOME%;%PATH%

REM === NETTOYAGE DES .pyc ===
del "%BASEDIR%\GENEPI\env\*.pyc" >nul 2>&1

REM === COPIE DES FICHIERS DE CONFIG SELON L'ENVIRONNEMENT ===
if "%ENVIRONMENT%"=="SAB" (
    copy /y "%BASEDIR%\GENEPI\env\sab_env\config.ini" "%BASEDIR%\GENEPI\env\config.ini"
    copy /y "%BASEDIR%\GENEPI\env\sab_env\init_sab_env.py" "%BASEDIR%\GENEPI\env\config.py"
) else (
    copy /y "%BASEDIR%\GENEPI\env\sae_env\config.ini" "%BASEDIR%\GENEPI\env\config.ini"
    copy /y "%BASEDIR%\GENEPI\env\sae_env\init_sae_env.py" "%BASEDIR%\GENEPI\env\config.py"
)

REM === POSITIONNEMENT DU DOSSIER COMME RÉPERTOIRE COURANT ===
cd /d "%BASEDIR%"

REM === LANCEMENT DU SCRIPT PYTHON PASSÉ EN ARGUMENT ===
"%PYTHONHOME%\python.exe" %1

pause
"""
    genepi_bat_file = os.path.join(
        etat_work_directory,
        'GenepiAuto',
        "GENEPIAuto_Launcher.bat"
    )


    with open(genepi_bat_file, "w", encoding="utf-8") as f:
        f.write(content)
