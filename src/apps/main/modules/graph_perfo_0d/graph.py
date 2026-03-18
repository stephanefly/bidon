import numpy as np
import pandas as pd
from bokeh.embed import components
from bokeh.layouts import gridplot,column
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LassoSelectTool,
    Slope,
    Span,
    TapTool,
    CustomJS,
    Div
)
from bokeh.events import MouseMove
from bokeh.plotting import figure
from apps.main.models import Cas
from apps.main.modules.gestion_projets.tools import get_symbol_list
from apps.main.modules.graph_perfo_0d.js_bokeh import (
    callback_selection,
    callback_surbrillance,
)


def build_graph_configuration(etat, dict_data_cas):

    key = list(dict_data_cas.keys())[0]  # première clé
    df = dict_data_cas[key]

    is_only_stator = df["is_only_stator"].iloc[0]
    variable = "Cd" if is_only_stator else "Etapol"

    new_conf = []
    for c in etat.graph_configuration:
        x_name = c["x_axis"]
        y_name = c["y_axis"]

        if x_name == "Cd" or x_name == "Etapol" or x_name == "Cd/Etapol":
            x_name = variable
        if y_name == "Cd" or y_name == "Etapol" or y_name == "Cd/Etapol":
            y_name = variable

        new_conf.append({"x_axis": x_name, "y_axis": y_name})

    etat.graph_configuration = new_conf
    etat.save()


def generate_graphs(etat, dict_data_cas, index, plane_dict):

    graphs = []
    source_shared = []
    df_all = []

    build_graph_configuration(etat, dict_data_cas)

    for graph in etat.graph_configuration:
        p, df, line_sources, source, scatter = initialise_graph_od(
            etat,
            dict_data_cas,
            graph
        )
        graphs.append(p)
        df_all.append(df)
        source_shared.append(source)

        callback_selection(source, scatter, etat.id)

    callback_surbrillance(source_shared)

    titre_plan_html = generate_titre_plan_html(etat, plane_dict)

    df_legend = pd.concat(df_all, ignore_index=True)
    legend_html = generate_legend_html(df_legend)

    grid = gridplot(graphs, ncols=3, sizing_mode="stretch_width")
    script, div = components(grid)

    return {
        "id": f"tab-{index + 1}",
        "active": index == 0,
        "script": script,
        "div": div,
        "legend_html": legend_html,
        "titre_plan_html": titre_plan_html,
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

    zoom_coeff = 0.001
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
    if "moyenne_type" not in combined_df.columns:
        combined_df["moyenne_type"] = ""


    # 4) Source principale
    source = ColumnDataSource(data=dict(
        x=combined_df[x_name],
        y=combined_df[y_name],
        color=combined_df["element_color"],
        cas_name=combined_df["name"],
        kd=combined_df["kd"],
        cas_id=combined_df["id"],
        marker=combined_df["marker"],
        moyenne_type=combined_df["moyenne_type"],
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

    # 7) Lignes ordonné par Qcorr
    line_sources = []

    if "group" in combined_df.columns:
        for _, group in combined_df.groupby("group"):
            group = group.copy()

            # Calcul Qcorr si nécessaire et possible
            if "Qcorr" not in group.columns and {"Qcorr_ref", "Pi",
                                                 "tau"}.issubset(group.columns):
                group["Qcorr"] = group["Qcorr_ref"] * (group["tau"] ** 0.5) / \
                                 group["Pi"]

            # Tri si Qcorr dispo, sinon on laisse l'ordre
            group_sorted = group.sort_values(
                "Qcorr") if "Qcorr" in group.columns else group

            # Source Bokeh
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

    # 9. hover partout
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

    # 10. Outils
    # Tooltip sur les point
    hover_point = HoverTool(
        tooltips=[("X", "@x"), ("Y", "@y"), ("KD", "@kd"), ("moy", "@moyenne_type"),("Cas", "@cas_name")],
        renderers=[scatter],
        attachment="left",
    )
    p.add_tools(hover_point)

    # Tooltip Lassot
    lasso = LassoSelectTool()
    p.add_tools(lasso)
    tap_tool = TapTool()
    p.add_tools(tap_tool)
    p.toolbar.active_drag = lasso

    # Tooltip générique sur toute la surface du plot

    info = Div(
        text="<b>X:</b> — , <b>Y:</b> —",
        width=150,
        height=25,
        styles={
            "position": "absolute",
            "top": "0px",
            "right": "0px",
            "background-color": "rgba(255, 255, 255, 0.75)",
            "border": "1px solid #999",
            "border-radius": "6px",
            "padding": "2px 4px",
            "font-size": "12px",
            "pointer-events": "none",
            # IMPORTANT : ne bloque pas les interactions
            "z-index": "10",
        },
    )

    p.js_on_event(MouseMove, CustomJS(args=dict(div=info), code="""
        if (cb_obj.x == null || cb_obj.y == null) return;
        div.text = `<b>X:</b> ${cb_obj.x.toFixed(3)} , <b>Y:</b> ${cb_obj.y.toFixed(3)}`
    """))

    layout = column(info, p, sizing_mode="stretch_width")

    return layout, combined_df, line_sources, source, scatter


def generate_legend_html(df):
    # On fusionne proprement les colonnes nécessaires
    legend_items = (
        df
        .groupby(["group", "element_color", "marker"])
        .agg({
            "kd": lambda x: set(x),
            "moyenne_type": lambda x: set(x)
        })
        .reset_index()
        .to_dict("records")
    )
    html = ["<div class='legend-container'>"]

    for item in legend_items:

        group = item["group"]
        color = item["element_color"]
        marker = item["marker"]
        symbol = get_symbol_list()[marker]["symbol"]

        # Legende KD
        kd_value = round(next(iter(item["kd"])), 4)

        # moyenne_type
        moyenne_type = item["moyenne_type"]
        moy_text = f" | moy = {next(iter(moyenne_type))}" if item["moyenne_type"] else ""

        # Construction du bloc HTML
        html.append(
            f"<div class='legend-item' style='color: {color}; font-weight: bold'>"
            f"<span class='legend-color'></span>{symbol} {group} (KD={kd_value} {moy_text})"
            "</div>"
        )

    html.append("</div>")
    return "\n".join(html)


def generate_titre_plan_html(etat, plane_dict):

    cas_list = Cas.objects.filter(pk__in=plane_dict.keys())

    # On vérifie si tous les cas sont des excel
    if cas_list and (
            all(cas.iso_vitesse.file_type == "excel" for cas in cas_list)
            or
            all(cas.obj_type == "cas_utilisateur" for cas in cas_list)
    ):
        return ""

    else:
        rows_html = ""

        for cas_id, value in plane_dict.items():
            cas = Cas.objects.get(pk=cas_id)
            if cas.iso_vitesse.file_type == 'hdf':

                if etat.plan_amont_selected not in value[0] or \
                   etat.plan_aval_selected not in value[1]:

                    rows_html += (
                        "<tr>"
                            f"<td style='color:{cas.iso_vitesse.color}; font-weight:600;'>"
                                f"{cas.name} (hdf)"
                            "</td>"
                            f"<td class='text-center mb-4'>"
                                f"{value[0]} <span class='text-muted'>vs</span> {value[1]}"
                            "</td>"
                        "</tr>"
                    )

        # Table seulement si on a des lignes
        table_html = ""
        if rows_html:
            table_html = (
                "<table class='table table-borderless align-middle mb-0'>"
                    "<thead>"
                        "<tr class='border-bottom'>"
                            "<th class='text-width'>Nom du Cas</th>"
                            "<th class='text-center'>Plans Utilisés</th>"
                        "</tr>"
                    "</thead>"
                    "<tbody>"
                        f"{rows_html}"
                    "</tbody>"
                "</table>"
            )

        titre_plan_html = (
            "<div class='card shadow-sm border-0'>"
                "<div class='card-body px-4 py-4'>"
    
                    "<div class='text-center'>"
                        f"<h4 class='fw-bold'>"
                            f"<span class='text-muted'>Plans hdf : </span>{etat.plan_amont_selected} "
                            "<span class='text-muted'>vs</span> "
                            f"{etat.plan_aval_selected}"
                        "</h4>"
                    "</div>"
    
                    f"{table_html}"
    
                "</div>"
            "</div>"
        )

        return titre_plan_html





