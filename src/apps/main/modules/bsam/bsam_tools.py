import yaml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bsamreader import ThroughFlow
from bsamreader.plotting.plot_bsam import plot_bsam

from apps.main.models import Cas
from apps.main.modules.gestion_projets.tools import get_symbol_list


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

    # Sauvegarde et affichage
    image_path = revue_veine.get_image_path()
    fig.savefig(image_path, dpi=600)

    return image_path


def plot_caracteristics_bsam(cache_cas, carac, hauteurs):
    print(carac)

    y_min_all = None
    y_max_all = None

    fig, axs = plt.subplots(1, carac["Nb_hauteur_base"], figsize=(15, 5))
    axs = np.atleast_1d(axs)

    all_data = []  # Stocker les données pour l'export Excel

    symbols = get_symbol_list()
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
            symbole = symbols[cas.iso_vitesse.marker]["mpl"]
            axs[i].plot(x_values, y_data, marker=symbole, color=cas.iso_vitesse.color)
            axs[i].set_xlabel(x_label)
            axs[i].set_ylabel(var_name)
            if carac["Nb_hauteur_base"] != 1:
                axs[i].set_title(f"hH={100 * hauteurs[i]}%")
            axs[i].set_xlim(min(x_values), max(x_values))
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


def load_carac_config(nb_graph,
                      filepath=r"src\apps\main\modules\bsam\carac_config.yaml",):
    with open(filepath, encoding="utf-8") as file:
        config = yaml.safe_load(file)
    for carac in config.get("lst_carac", []):
        if not carac.get("Nb_hauteur_base"):
            carac["Nb_hauteur_base"] = nb_graph
    return config.get("lst_carac", [])
