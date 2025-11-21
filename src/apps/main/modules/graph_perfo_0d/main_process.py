import json
import os

import pandas as pd
from apps.main.models import Cas, Etat, IsoVitesse
from apps.main.modules.graph_perfo_0d.gestion_data import (export_data_html, export_data_excel, make_json_serializable)
from apps.main.modules.graph_perfo_0d.graph import generate_graphs

from apps.main.modules.graph_perfo_0d.calcul_perfo import process_data


def process_graph_perfo_0d(etat, data, cache_path):

    # GENERATION DES DONNEES
    data_cache = {}
    for iso_vitesse in IsoVitesse.objects.filter(etat=etat):

        if iso_vitesse.used_cas() == 0:
            continue

        print(f" * On traite l'iso {iso_vitesse.name} (Type={iso_vitesse.file_type})")

        data_cache = process_data(data_cache, iso_vitesse)

    # GENERATION des PAGES de GRAPH
    tabs = []
    for index, etage in enumerate(list(data_cache.keys())):
        tab_data = generate_graphs(etat, data_cache[etage], index)
        tab_data["label"] = etage
        tabs.append(tab_data)
    data["tabs"] = tabs

    # EXPORT DES GRAPH
    export_data_html(data, etat)

    # EXPORT FORMAT EXCEL
    export_data_excel(data_cache, etat)

    # GESTION DU CACHE
    # etat.clean_old_cache_files()
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False,
                  default=make_json_serializable)

    return data