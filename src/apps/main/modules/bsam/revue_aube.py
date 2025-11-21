import os
import datetime
from pathlib import Path
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
import os
import shutil
import subprocess
from pathlib import Path

from apps.main.models import UtilitaireConfiguration
from apps.main.modules.graph_perfo_0d.get_config_from_row import rename_row


def create_bat_shortcut(revue_aube, user):

    genepi_path = UtilitaireConfiguration.objects.get(user=user).genepi_path

    # Ton batch existant
    batch_file = Path(os.path.join(genepi_path, "GENEPIbatch.bat")) # adapter si besoin
    print(batch_file)

    # Où déposer le .lnk
    path_lnk = Path(revue_aube.work_dir) / "GENEPIbatch.lnk"

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
    print(f"[OK] Raccourci créé : {path_lnk}")


def _py_str(s: str) -> str:
    """Retourne une chaîne Python correctement quotée/échappée (pour le .py)."""
    if s is None:
        return "''"
    return repr(str(s))


def _split_coupes(val):
    """'01,11,15,19,29' -> ['01','11','15','19','29'] (préserve zéros)."""
    if not val:
        return []
    parts = [p.strip() for p in str(val).split(",") if p.strip()]
    return parts


def _bool01(b) -> str:
    return "1" if bool(b) else "0"


def create_py_file(revue_aube, aubes, user):

    genepi_auto_path = UtilitaireConfiguration.objects.get(user=user).genepi_auto_path

    list_str = [str(rename_row(_py_str(a.label_bsam))) for a in aubes if
                a.label_bsam]
    joined_str = ', '.join(f"'{v}'" for v in list_str)

    titre_pres = revue_aube.name
    header = f"""#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------
# TITRE DE LA PRESENTATION

TitrePres = {_py_str(titre_pres)}

#-------------------------------------------------------------------------------------------------------------------
# CHOIX DES EXPORT DE LA PRESENTATION

ExportPDF = 1
ExportExcel = 1
ExportPPT = 0

#-------------------------------------------------------------------------------------------------------------------
# CHOIX DES POST-TRAITEMENTS A EFFECTUER

Trace_InfosCas = 1             # Permet d'avoir le tableau recapitulatif des cas traités dans genepi.
Trace_InfosPlanUtilisateur = 0 # Permet d'avoir le tableau 'plus ou moins' récapitulatif des plans utilisés dans genepi.
#--------------
Trace_QualiteMaillage = 0      # Permet d'avoir le tableau recapitulatif de la qualité du maillage AG5.
Trace_VisuQualiteMaillage = 0  # Permet d'importer les visualisations du maillage sorti automatiquement par le script AG5Auto --> A Faire
#--------------
Trace_ConvDebit = 0            # Permet de tracer l'evolution du débit d'un calcul cannelle --> Post-traitement long et pas trés propre
Trace_ConvResidus = 0          # Permet de tracer l'evolution des résidus d'un calcul cannelle --> Post-traitement long et pas trés propre

#--------------
Trace_ParVariable = 0          # Si Trace_ParVariable = 1, alors on groupe les tracés par variables (si plusieurs roues alors une page par variable avec toutes les roues tracés)
#--------------
Trace_LoisGeom = 1             # Permet de tracer les lois geometriques d'un aubage en passant par CARMA (Necessite l'acces à la base aube)
Trace_Perfos0D = 0             # Permet de tracer les perfos 0D (Redmine en cours pour traiter les cas multi-aubes)
Trace_ProfilsRadiaux = 0       # Permet de tracer les profils Radiaux par roue
Trace_ProfilVsCorde = 0        # Permet de tracer les répartitions de grandeurs le long de la corde (Machis/Hi/Ps...)
Trace_ProfilsRadiauxAngle = 0  # Permet de tracer les profils radiaux issuent du fichier angle_BA_BF.xls (inc/efp/Bsq1/bsq2/dli/Zweiffel)
Trace_ProfilAzimuthaux = 0     # Permet de tracer les profils azimuthaux issus d'un calcul cannelle postraité avec Antares
Trace_Polaire = 0              # Permet de tracer des grandeurs selon le formalisme polaire (Valeurs extraite à 50% et les plans pour le tracé des variables sont dissociés)
#--------------
Trace_EvolutionParois = 0
Trace_EvolutionAxiale = 0
Trace_EvolutionMeridienne = 0

#-------------------------------------------------------------------------------------------------------------------
# LISTE DES AUBES A TRACER : --> NE DOIT PAS ETRE VIDE  !!!!!
DicoLabelAube2Trace = {{'Total': [{joined_str}], 'Primaire': [], 'Secondaire': []}}

#-------------------------------------------------------------------------------------------------------------------
# PRESENCE DE CAS MISES
MisesCase = False  # Permet d'utiliser une parametrisation specifique pour les profils radiaux (DicoXYVarProfilsRadiaux2Trace_Mises).

#-------------------------------------------------------------------------------------------------------------------
# INFORMATION SUR LES CAS DE CALCUL CFD (NS3D/NS2.75D/MISES/AZTEC) ET/OU BSAM ET/OU CARMA A TRACER

#      - 'Couleur': 'Black' ,'Red' ,'Blue' ,'Green' ,'Violet' ,'Pink' ,'Orange' ,'Yellow' ,'OrangeRed' ,'Maroon' ,'Grey' ,'Cyan' ,'DarkBlue' ,'RoyalBlue' ,'LightBlue' ,'LightGreen' ,'DarkGreen' ,'DarkCyan' ,'Brown'
#      - 'Ligne'  : 'SolidLine', 'DashLine', 'DotLine', 'DashDotLine', 'DashDotDotLine', 'NoPen'
#      - 'Symbole': 'o', '+', 's', 't', 'd', None

"""
    blocks = []
    for i, a in enumerate(aubes, start=1):
        coupes = _split_coupes(a.coupe_dessin)
        coupes_txt = "[" + ", ".join(_py_str(x) for x in coupes) + "]"

        bloc = []
        prefix = f"InfoCasCARMA_{i}"
        bloc.append(f"{prefix} = {{}}")
        bloc.append(f"{prefix}['Aube'] = {_py_str(a.aube)}")
        bloc.append(f"{prefix}['Calage'] = {float(a.calage_deg or 0.0)}")
        bloc.append(f"{prefix}['CheminBsam'] = r'{a.fichier_bsam}'")
        bloc.append(f"{prefix}['Couleur'] = {_py_str(str(a.color or '').lower())}")
        bloc.append(f"{prefix}['CoupesDessin'] = {coupes_txt}")
        bloc.append(f"{prefix}['Gcolter'] = 1")
        bloc.append(f"{prefix}['Grille'] = {_py_str(a.version or 'S1')}")
        bloc.append(f"{prefix}['HauteurBSAM'] = 1")
        bloc.append(f"{prefix}['InverserBsam'] = {_bool01(a.inversion_bsam)}")
        bloc.append(f"{prefix}['Ligne'] = 'SolidLine'")
        bloc.append(f"{prefix}['NbAube'] = {int(getattr(a, 'nb_aube', 44) or 44)}")
        bloc.append(f"{prefix}['Projet'] = {_py_str(a.projet)}")
        bloc.append(f"{prefix}['RedecouperAube'] = 1")
        bloc.append(f"{prefix}['RetournerAube'] = {_bool01(a.inversion_aube)}")
        bloc.append(f"{prefix}['RetournerAubeGcolter'] = 0")
        bloc.append(f"{prefix}['SweepDiedre'] = 1")
        bloc.append(f"{prefix}['Symbole'] = 'o'")
        if not a.titre_cas == "":
            bloc.append(f"{prefix}['TitreCas'] = {_py_str(a.titre_cas)}")
        else:
            titre = "_".join([x for x in [a.projet, a.version, a.aube] if x])
            bloc.append(f"{prefix}['TitreCas'] = {_py_str(titre)}")
        bloc.append(f"{prefix}['TraceBSAM'] = 1")
        type_coupe = getattr(a, "type_coupe_nbre_ldc", "CQ")
        bloc.append(f"{prefix}['TypeCoupe'] = [{_py_str(type_coupe)}]")
        bloc.append(f"{prefix}['Version'] = {_py_str(a.version)}")
        bloc.append(f"{prefix}['Xemp'] = {float(getattr(a, 'xemp', 112.0) or 112.0)}")
        bloc.append(f"{prefix}['lienXML'] = r'{a.lien_xml}'")
        bloc.append("\n")
        blocks.append("\n".join(bloc) + "\n")


    tail = f"""
#-------------------------------------------------------------------------------------------------------------------
# RENOMMAGE DES PLANS DE POST-TRAITEMENT:
# PERMET DE POUVOIR COMPARER DES PLANS DIFFERENT ENTRE EUX EN PASSANT PAR UN NOM DE PLAN INTERMEDIAIRE
# SI LA CLEF 'RenommagePlan' EST DEFINIE DANS DICO InfoCas ALORS LES PLANS CI DESSOUS NE SONT PAS PRIS EN COMPTE 

# Pour les cas CFD :
PlanCFD_AmontPerfo='Inlet'
PlanCFD_AvalPerfo='Outlet'
PlanCFD_ProcheBA='(BA)'
PlanCFD_ProcheBF='(BF)'
PlanCFD_LoinBA='Inlet'
PlanCFD_LoinBF='Outlet'

# Pour les cas BSAM :
PlanBSAM_AmontPerfo='(BA)'
PlanBSAM_AvalPerfo='(BF)'
PlanBSAM_ProcheBA='(BA)'
PlanBSAM_ProcheBF='(BF)'
PlanBSAM_LoinBA='(BA-2)'
PlanBSAM_LoinBF='(BF+2)'

# Plan pour Gcolter :
PlanGcolter_Amont='(BA)'
PlanGcolter_Aval='(BF)'

#-------------------------------------------------------------------------------------------------------------------
# IMPORT DES DICTIONNAIRES DE TRACE
import sys

genepi_dico_path = r'{os.path.dirname(revue_aube.dico_genepi_auto)}'
if genepi_dico_path not in sys.path:
    sys.path.append(genepi_dico_path)

from {os.path.splitext(os.path.basename(revue_aube.dico_genepi_auto))[0]} import *

#-------------------------------------------------------------------------------------------------------------------
# CHEMIN VERS LE SCRIPT GENEPIAUTO
exec(open(r'{genepi_auto_path}', 'r', encoding='utf8').read(), locals())
"""

    content = header + "".join(blocks) + tail

    path_ink = Path(revue_aube.work_dir) / "presentation_revue_aube.py"
    path_ink.write_text(content, encoding="utf-8")

    return redirect("info_revue_aube", revue_aube_id=revue_aube.id)

