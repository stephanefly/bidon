from bokeh.models import Span
import pandas as pd
from bokeh.embed import components
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, HoverTool, LassoSelectTool, TapTool
from bokeh.plotting import figure

from apps.main.modules.graph_perfo_0d.js_bokeh import (
    callback_selection,
    callback_surbrillance,
)

from apps.main.modules.gestion_projets.tools import get_symbol_list
from apps.main.modules.graph_perfo_0d.gestion_data import find_key_in_data
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, LassoSelectTool, TapTool, Span, Slope


def generate_graphs(etat, dict_data_cas, index):

    graphs = []
    source_shared = []

    variable = "Cd" if find_key_in_data(dict_data_cas, 'is_only_stator') else "Etapol"

    configurations = [
        {"x_axis": "Qcorr_ref", "y_axis": "Pi"},
        {"x_axis": variable, "y_axis": "Pi"},
        {"x_axis": "Qcorr", "y_axis": "Pi"},
        {"x_axis": "Qcorr_ref", "y_axis": variable},
        {"x_axis": variable, "y_axis": "PisQcorr_ref"},
        {"x_axis": "Qcorr", "y_axis": variable},
    ]


    for graph in configurations:
        p, df, line_sources, source, scatter = initialise_graph_od(
            etat,
            dict_data_cas,
            graph
        )
        graphs.append(p)

        source_shared.append(source)

        callback_selection(source, scatter, etat.id)

    callback_surbrillance(source_shared)

    grid = gridplot(graphs, ncols=3, sizing_mode="stretch_width")
    script, div = components(grid)
    legend_html = generate_legend_html(df)

    return {
        "id": f"tab-{index + 1}",
        "active": index == 1,
        "script": script,
        "div": div,
        "legend_html": legend_html,
    }




def initialise_graph_od(etat, dict_data_cas, graph):
    # 1) Extraire uniquement les DataFrames du dict (mélange DF + métadonnées)
    frames = [
        v for v in dict_data_cas.values()
        if isinstance(v, pd.DataFrame) and not v.empty and not v.isna().all().all()
    ]
    if len(frames) == 0:
        # Graphique vide mais fonction robuste
        p = figure(height=375, sizing_mode="stretch_width")
        return p, pd.DataFrame(), [], ColumnDataSource(dict(x=[], y=[])), None

    combined_df = pd.concat(frames, ignore_index=True)

    zoom_coeff = 0.01
    x_name = graph["x_axis"]
    y_name = graph["y_axis"]

    # 2) Limites axes robustes aux NaN
    x_data = pd.to_numeric(combined_df[x_name], errors='coerce').to_numpy()
    y_data = pd.to_numeric(combined_df[y_name], errors='coerce').to_numpy()

    if len(x_data) == 0 or np.isnan(x_data).all():
        x_min, x_max = 0, 1
    else:
        x_min = (1 - zoom_coeff) * np.nanmin(x_data)
        x_max = (1 + zoom_coeff) * np.nanmax(x_data)
    if len(y_data) == 0 or np.isnan(y_data).all():
        y_min, y_max = 0, 1
    else:
        y_min = (1 - zoom_coeff) * np.nanmin(y_data)
        y_max = (1 + zoom_coeff) * np.nanmax(y_data)

    # 3) Colonnes optionnelles → valeurs par défaut
    if "element_color" not in combined_df.columns:
        combined_df["element_color"] = "#1f77b4"
    if "name" not in combined_df.columns:
        combined_df["name"] = ""
    if "id" not in combined_df.columns:
        combined_df["id"] = ""
    if "marker" not in combined_df.columns:
        combined_df["marker"] = "circle"

    # 4) Source principale
    source = ColumnDataSource(data=dict(
        x=combined_df[x_name],
        y=combined_df[y_name],
        color=combined_df["element_color"],
        cas_name=combined_df["name"],
        cas_id=combined_df["id"],
        marker=combined_df["marker"],
    ))

    # 5) Figure
    p = figure(
        height=375,
        x_axis_label=x_name,
        y_axis_label=y_name,
        x_range=[x_min, x_max],
        y_range=[y_min, y_max],
        sizing_mode="stretch_width",
        title=f"{y_name} vs {x_name}",
    )

    # 6) Nuage de points
    scatter = p.scatter(
        x="x", y="y", size=10, source=source,
        color="color", line_width=2, fill_alpha=1, marker="marker"
    )

    # 7) Lignes par groupe (si colonne 'group' dispo)
    line_sources = []
    if "group" in combined_df.columns:
        for _, group in combined_df.groupby("group"):
            # Tri prioritaire par x_name, fallback Qcorr si utile
            sort_key = x_name if x_name in group.columns else ("Qcorr" if "Qcorr" in group.columns else None)
            group_sorted = group.sort_values(by=sort_key) if sort_key else group

            line_source = ColumnDataSource(data=dict(
                x=group_sorted[x_name],
                y=group_sorted[y_name],
                color=group_sorted["element_color"],
                cas_name=group_sorted["name"],
                cas_id=group_sorted["id"],
            ))
            line_sources.append(line_source)

            p.line(
                x="x", y="y",
                line_width=2,
                line_color=str(group_sorted["element_color"].iloc[0]),
                source=line_source,
            )



    # 8.1) Lignes verticales pour data_type == "bsam" quand x_axis == "Qcorr"
    if "data_type" in combined_df.columns and x_name.strip() == "Qcorr":
        bsam_points = combined_df[combined_df["data_type"] == "bsam"]
        for _, row in bsam_points.iterrows():
            q_val = row.get("Qcorr", None)
            color = row.get("element_color", "#999999")
            if pd.notna(q_val):
                vline = Span(
                    location=float(q_val),
                    dimension="height",
                    line_color=color,
                    line_dash="dotted",
                    line_width=3
                )
                p.add_layout(vline)

    # 8.2) Quand l'axe X est Qcorr_ref
    if {"data_type", "is_only_stator", "Qcorr_ref", "element_color"}.issubset(
            combined_df.columns) \
            and x_name.strip() == "Qcorr_ref":

        bsam_rows = combined_df[combined_df["data_type"] == "bsam"]

        # Cas stators
        for _, row in bsam_rows[bsam_rows["is_only_stator"] == False].iterrows():
            qx, qy = row.get("Qcorr_ref"), row.get("Pi")
            if pd.notna(qx) and pd.notna(qy):
                p.add_layout(Slope(
                    gradient=float(qy) / float(qx),
                    y_intercept=0,
                    line_color=row.get("element_color", "#999999"),
                    line_dash="dotted",
                    line_width=3
                ))

        # Cas non-stators
        for _, row in bsam_rows[bsam_rows["is_only_stator"] == True].iterrows():
            q_val = row.get("Qcorr_ref")
            if pd.notna(q_val):
                p.add_layout(Span(
                    location=float(q_val),
                    dimension="height",
                    line_color=row.get("element_color", "#999999"),
                    line_dash="dotted",
                    line_width=3
                ))

    # 9) Outils
    p.add_tools(HoverTool(tooltips=[("X", "@x"), ("Y", "@y"), ("Cas", "@cas_name")]))
    lasso = LassoSelectTool()
    p.add_tools(lasso)
    tap_tool = TapTool()
    p.add_tools(tap_tool)
    p.toolbar.active_drag = lasso

    # 10. hover partout
    # --- Ajout de la zone "quad" invisible qui couvre tout le plot ---
    x_vals = [v for v in source.data['x'] if v is not None]
    y_vals = [v for v in source.data['y'] if v is not None]

    if not x_vals or not y_vals:
        # Si aucune donnée exploitable, bornes de repli
        box_left, box_right = 0, 1
        box_bottom, box_top = 0, 1
    else:
        box_left = min(x_vals) - 1
        box_right = max(x_vals) + 1
        box_bottom = min(y_vals) - 1
        box_top = max(y_vals) + 1

    box_source = ColumnDataSource(data=dict(
        left=[box_left],
        right=[box_right],
        bottom=[box_bottom],
        top=[box_top]
    ))

    quad_renderer = p.quad(
        left='left',
        right='right',
        bottom='bottom',
        top='top',
        fill_alpha=0,
        line_alpha=0,
        source=box_source
    )

    # Tooltip générique sur toute la surface du plot
    hover_global = HoverTool(
        tooltips=[("X", "$x{0.000}"), ("Y", "$y{0.000}")],
        renderers=[quad_renderer],
    )
    p.add_tools(hover_global)

    return p, combined_df, line_sources, source, scatter



def generate_legend_html(df):
    legend_items = df[["group", "element_color", "marker", "KD"]].drop_duplicates().to_dict("records")


    legend_html = "<div class='legend-container'>\n"

    symbol_dict = get_symbol_list()  # Appel unique, évite la répétition

    for item in legend_items:
        item_kd = item["KD"]
        if not item_kd or item_kd == 1 or str(item_kd).lower() == 'nan':
            kd = ""
        else:
            kd = f"(KD = {item_kd})"
        symbol = symbol_dict.get(item['marker'], {}).get('symbol', '?')
        legend_html += (
            f"<div class='legend-item' style='color: {item['element_color']}; font-weight: bold'>"
            f"<span class='legend-color'></span>{symbol} {item['group']} {kd}</div>\n"
        )
    legend_html += "</div>"
    return legend_html

