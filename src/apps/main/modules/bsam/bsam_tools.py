import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from bsamreader.plotting.plot_bsam import plot_bsam
from pathlib import Path
from apps.main.models import Cas
from apps.main.modules.gestion_projets.tools import get_symbol_list, \
    get_symbol_name_from_code
from django.conf import settings
import os
from datetime import datetime
from bsamreader import ThroughFlow

from apps.main.utils.paths import get_trace_veine_image_path


def make_veine_plot(revue_veine):
    # Liste des fichiers BSAM à traiter
    lst_cas_selected = Cas.objects.filter(
        revue_veine=revue_veine,
        used=True
    )

    fig, ax = plt.subplots(1, 1)
    for cas in lst_cas_selected:
        tf = ThroughFlow.from_bsam(cas.bsam_path)

        if cas.iso_vitesse:
            fig, ax = plot_bsam(
                fig, ax, tf, dx=0.0, color=cas.iso_vitesse.color, ls="-",
                marker=cas.iso_vitesse.marker
            )
        else:
            fig, ax = plot_bsam(
                fig, ax, tf, dx=0.0, color="black", ls="-"
            )

    # Ajout de la légende et labels
    ax.set_xlabel("X (m)")
    ax.set_ylabel("R (m)")
    # ax.set_title("Rayon - " + str(revue_veine.name))
    ax.axis("equal")
    plt.legend(fontsize=6)

    # Sauvegarde et affichage
    image_path = get_trace_veine_image_path(revue_veine)
    fig.savefig(image_path, dpi=600)
    plt.close(fig)

    return image_path



def plot_caracteristics_bsam(cache_cas, carac, hauteurs):

    y_min_all = None
    y_max_all = None

    fig, axs = plt.subplots(1, carac["Nb_hauteur_base"], figsize=(15, 5))
    axs = np.atleast_1d(axs)

    all_data = []  # Stocker les données pour l'export Excel

    var_name = carac["carac_name"]

    for item in cache_cas:
        cas = item["cas"]
        tf = item["tf"]
        calculators_all = item["calculators"]

        lst_rows = choix_des_rows(tf, carac)

        if carac["row_type"].lower() == "plans":
            first_row = lst_rows[0]
            row_key = getattr(first_row, "name", first_row)
            calculators = calculators_all[row_key]

            y_values = [calculators.calculer_values(var_name)]
            x_values = calculators.calculer_values("xplane")
            x_label = "X [m]"
            x_lim = None

        else:
            calculators = []
            for row in lst_rows:
                key = getattr(row, "name", row)
                calc = calculators_all.get(key)
                if calc is not None:
                    calculators.append(calc)

            values_list = []
            for calc in calculators:
                vals = calc.calculer_values(var_name)
                if vals is not None:
                    values_list.append(vals)

            if values_list:
                y_values = list(zip(*values_list))
            else:
                y_values = []

            # Longueur de veine adimensionnée
            if len(lst_rows) > 1:
                x_values = np.arange(len(lst_rows)) / (len(lst_rows) - 1)
                if carac["row_type"].lower() == "all":
                    x_values = x_values[1:]
            else:
                x_values = [0]
            x_label = "Nbe Aube Adim"
            x_lim = (0, 1)

        # Si aucune donnée -> on skip ce cas
        if not y_values:
            continue

        # Échelle globale
        y_min_all, y_max_all = echelle_plot(y_values, y_min_all, y_max_all)
        if y_min_all is None or y_max_all is None:
            y_min_all, y_max_all = 0, 1
        marge = (y_max_all - y_min_all) * 0.1

        # Tracé
        for i, y_data in enumerate(y_values):
            symbole = get_symbol_name_from_code(cas.iso_vitesse.marker)
            axs[i].plot(x_values, y_data, marker=symbole, color=cas.iso_vitesse.color)
            axs[i].set_xlabel(x_label)
            axs[i].set_ylabel(var_name)
            if carac["Nb_hauteur_base"] != 1:
                axs[i].set_title(f"hH={100 * hauteurs[i]}%")
            axs[i].set_xlim(x_lim)
            axs[i].grid(True)
            axs[i].set_ylim(y_min_all - marge, y_max_all + marge)

            # Données pour export Excel
            df = pd.DataFrame({
                "BSAM": cas.name,
                "X": x_values,
                f"Y (Hauteur {hauteurs[i]})": y_data,
            })
            all_data.append(df)

    plt.tight_layout()
    return plt, all_data


def choix_des_rows(tf, carac):
    if carac["row_type"] == "STATOR":
        lst_rows = [x for x in tf.rows_names if
                    tf.get_row_zone(x)[0].omega == 0]
    elif carac["row_type"] == "ROTOR":
        lst_rows = [x for x in tf.rows_names if
                    tf.get_row_zone(x)[0].omega != 0]
    else:
        lst_rows = tf.rows_names
    return lst_rows


def echelle_plot(y_values, y_min_all, y_max_all):
    y_values_non_empty = [lst for lst in y_values if lst]

    if not y_values_non_empty:
        return y_min_all, y_max_all  # ou (None, None)

    y_min_bsam = min(map(min, y_values_non_empty))
    y_max_bsam = max(map(max, y_values_non_empty))

    y_min_all = min(y_min_bsam, y_min_all) if y_min_all is not None else y_min_bsam
    y_max_all = max(y_max_bsam, y_max_all) if y_max_all is not None else y_max_bsam

    return y_min_all, y_max_all


def get_bsam_kd(case_obj):
    """
    KD de la Premiere row de la première zone
    """

    tf = ThroughFlow.from_bsam(case_obj.bsam_path)
    # TODO : Rechercher le kd du entry row du global
    row0 = tf.zones[0].rows[0]
    kd_bsam = row0.inlet.kd

    return kd_bsam


def bsam_file_test(bsam_file_path):

    try:
        tf = ThroughFlow.from_bsam(bsam_file_path)
        result_test = "Bsam lisible par Bsam Reader"
        return True, result_test
    except:
        result_test = "Bsam non lisible par Bsam Reader"
        return False, result_test


def get_nb_aube_and_xemp(aube):
    """
    Retourne (nb_aubes, xemp) pour une aube donnée à partir du BSAM.
    xemp est retourné en mm.
    """

    tf = ThroughFlow.from_bsam(aube.fichier_bsam)

    for zone in tf.zones:
        for row in zone.rows:
            if row.name != aube.label_bsam:
                continue

            # Nb d’aubes
            nb_aubes = row.z

            # Récupération des données de la station courante
            section = row.stations[row._istack]
            data = {
                feature: getattr(section, feature, None)
                for feature in getattr(section, "features_1d", [])
            }

            # Xemp en mm
            xemp = data["x"][0] * 1000

            return nb_aubes, xemp