
from pathlib import Path
from io import BytesIO
from datetime import datetime
import base64

import pandas as pd
from bsamreader import ThroughFlow

from apps.main.models import Cas
from apps.main.modules.bsam.bsam_tools import plot_caracteristics_bsam
from apps.main.modules.bsam.calcul_carac import CaracCalculator


def generate_html_header(revue_veine_name):
    return f"""<!DOCTYPE html>
<html lang='fr'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Revue Veine</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #fff0ff;
            text-align: center;
            margin: 0;
            padding: 20px;
            display: flex;
        }}
        .sommaire-sidebar {{
            position: fixed;
            left: 0;
            top: 0;
            bottom: 0;
            width: 250px;
            background: #f9f9f9;
            padding: 20px;
            border-right: 2px solid #ccc;
            box-shadow: 2px 0px 10px rgba(0, 0, 0, 0.2);
            text-align: left;
            overflow-y: auto;
        }}
        .sommaire-grid {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .sommaire-card {{
            display: block;
            background: #ffffff;
            text-decoration: none;
            color: #333;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .sommaire-card:hover {{
            transform: scale(1.05);
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.2);
        }}
        .sommaire-card-content {{
            text-align: center;
        }}
        .sommaire-card h3 {{
            margin: 0;
            font-size: 16px;
            color: #007bff;
        }}
        .sommaire-card p {{
            margin: 5px 0 0;
            font-size: 14px;
            color: #666;
        }}
        .content-container {{
            margin-left: 300px;
            width: calc(100% - 270px);
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .card {{
            background: white;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25);
            padding: 20px;
            width: 100%;
            max-width: 1400px;
            margin-bottom: 20px;
            box-sizing: border-box;
        }}
        img {{
            max-width: 100%;
            border-radius: 5px;
        }}
        h2 {{
            color:#4d4c4d
        }}
        h1 {{
            background-color: #e6e6e6;
            width: 100%;
            padding: 15px;
        }}
        footer {{
            width: 100%;
            background: #222;
            color: white;
            text-align: center;
            padding: 15px 0;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class='sommaire-sidebar'>
        <h2 style="text-align: center">Liste des caractéristiques</h2>
        <div class='sommaire-grid'>
        </div>
    </div>
    <div class='content-container'>
        <h1>Revue Veine : {revue_veine_name}</h1>
"""

def generate_html_sommaire(lst_carac):
    sommaire_links = "".join(
        f'''
        <a href="#{carac["carac_name"]}-{carac["row_type"]}" class="sommaire-card">
            <div class="sommaire-card-content">
                <h3>{carac["carac_name"]}</h3>
                <p>{carac["row_type"]}</p>
            </div>
        </a>
        '''
        for carac in lst_carac
    )
    return sommaire_links

def generate_html_card(carac, img_base64, lst_cas):

    bsam_links = "".join(
        f'<div style="border: 1px solid {cas.iso_vitesse.color}; '
        f'border-radius: 10px; padding: 8px; margin: 8px; '
        f'color: {cas.iso_vitesse.color}; '
        f'display: inline-block; min-width: 100px; text-align: center;">'
        f' {cas.name} </div>'
        for i, cas in enumerate(lst_cas)
    )

    return f"""
    <div class='card' id='{carac["carac_name"]}-{carac["row_type"]}'>
        <h2>{carac["carac_name"]} - {carac["row_type"]}</h2>
        <div style="display: flex; flex-wrap: wrap; gap: 5px; justify-content: center; align-items: center;">{bsam_links}</div>
        <img src='data:image/png;base64,{img_base64}' alt='Graphique {carac["carac_name"]}' />
    </div>
    """



def generate_footer():
    return """
        <footer>
        Généré par <strong>TRUNKS</strong> | <strong>YRKC2</strong>
    </footer>
    """


def calculators_cache(lst_cas, hauteurs):
    cache_cas = []

    for cas in lst_cas:
        tf = ThroughFlow.from_bsam(cas.bsam_path)
        calculators_all = {}

        for zone in tf.zones:
            for row in zone.rows:
                # row_key = nom de la ligne si dispo, sinon l'objet lui-même
                row_key = getattr(row, "name", row)
                calculators_all[row_key] = CaracCalculator(tf, row_key, hauteurs)

        cache_cas.append({
            "cas": cas,
            "tf": tf,
            "calculators": calculators_all,
        })

    return cache_cas


def generate_full_data(lst_carac, revue_veine, hauteurs):
    """
    1) Calcule cache_cas
    2) Génère le HTML complet
    3) Construit all_excel_data pour export multi-feuilles

    Retourne:
        html_content (str)
        all_excel_data (dict[str, DataFrame])
    """

    lst_cas = Cas.objects.filter(revue_veine=revue_veine, used=True)

    # Cache des courbes
    cache_cas = calculators_cache(lst_cas, hauteurs)

    # HEADER + sommaire
    html_content = generate_html_header(revue_veine.name)
    html_content = html_content.replace(
        "<div class='sommaire-grid'>",
        f"<div class='sommaire-grid'>{generate_html_sommaire(lst_carac)}"
    )

    # Dictionnaire final: { nom_feuille : DataFrame }
    all_excel_data = {}

    # Boucle principale
    for carac in lst_carac:

        plt_obj, all_data = plot_caracteristics_bsam(cache_cas, carac, hauteurs)

        # Intégration image dans HTML
        buffer = BytesIO()
        plt_obj.savefig(buffer, format="png")
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        html_content += generate_html_card(carac, img_base64, lst_cas)

        # Construction des données Excel
        if all_data:
            layout_data(all_data, carac, all_excel_data)

    html_content += generate_footer()

    return html_content, all_excel_data


def layout_data(all_data, carac, all_excel_data):

    # Fusionner tous les DataFrames
    df_all = pd.concat(all_data, ignore_index=True)

    # Convertir X (virgule -> point -> float)
    df_all["X"] = df_all["X"].astype(str).str.replace(",", ".").astype(
        float)

    # --- Trouver dynamiquement toutes les colonnes Y (Hauteur XXX) ---
    y_cols = [c for c in df_all.columns if c.startswith("Y (Hauteur")]

    # Ajouter les colonnes manquantes (s'il manque des hauteurs dans certains blocs)
    for col in y_cols:
        if col not in df_all.columns:
            df_all[col] = None

    # --- Regroupement dynamique, sans nom de colonnes en dur ---
    agg_dict = {col: "max" for col in y_cols}

    df_final = (
        df_all
        .sort_values(["BSAM", "X"])
        .groupby(["BSAM", "X"])
        .agg(agg_dict)
        .reset_index()
    )
    # Nom d’onglet (31 char max)
    sheet_name = carac["carac_name"][:31]

    # Stockage dans le dict final
    all_excel_data[sheet_name] = df_final

    return all_excel_data


def export_excel_revue_veine(revue_veine, all_excel_data):
    """
    Écrit le fichier Excel dans le répertoire de travail de la revue.

    Retourne:
        path_export_excel_revue (Path)
    """
    work_repo = Path(revue_veine.directory)
    work_repo.mkdir(parents=True, exist_ok=True)

    output_file = f"data-{revue_veine.name}-{datetime.now().strftime('%Y%m%d-%H%M')}.xlsx"
    path_export_excel_revue = work_repo / output_file

    print(all_excel_data)

    with pd.ExcelWriter(path_export_excel_revue, engine="openpyxl", mode="w") as writer:
        for sheet_name, df in all_excel_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    return path_export_excel_revue
