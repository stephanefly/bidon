import json
import os
from apps.main.models import IsoVitesse
from apps.main.modules.graph_perfo_0d.calcul_perfo import process_data
from apps.main.modules.graph_perfo_0d.gestion_data import (
    export_data_excel,
    export_data_html,
    make_json_serializable,
    make_planes_tab_data
)
from apps.main.modules.graph_perfo_0d.graph import generate_graphs
from pathlib import Path

def process_graph_perfo_0d(etat, data, cache_path):
    # GENERATION DES DONNEES
    data_cache = {}
    all_plane_dict = {}

    for iso_vitesse in IsoVitesse.objects.filter(etat=etat):

        if iso_vitesse.used_cas() == 0:
            continue

        data_cache, plane_dict = process_data(data_cache, iso_vitesse)

        # fusion propre
        for key, value in plane_dict.items():
            all_plane_dict.setdefault(key, {}).update(value)

    # GENERATION des Titre des ETAGES
    all_plane_dict = make_planes_tab_data(all_plane_dict)

    # GENERATION des PAGES de GRAPH
    tabs = []
    for index, etage in enumerate(list(data_cache.keys())):
        tab_data = generate_graphs(etat, data_cache[etage], index, all_plane_dict[etage])
        tab_data["label"] = etage
        tabs.append(tab_data)
    data["tabs"] = tabs

    # EXPORT GRAPH et FORMAT EXCEL
    perfo_dir = Path(etat.work_directory) / "Perfo0D"
    perfo_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(perfo_dir, 0o775)
    export_data_html(data, etat)
    export_data_excel(data_cache, etat)

    # GESTION DU CACHE
    # etat.clean_old_cache_files()
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False,
                  default=make_json_serializable)

    return data
