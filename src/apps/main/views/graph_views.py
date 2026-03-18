import os.path
from datetime import datetime
from config.settings.base import PATH_STYLE
from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from apps.main.models import Cas, Etat, RevueVeine
from apps.main.modules.genepi.create_genepi_from_perfo0D import (
    create_genepi_file,
)
from apps.main.modules.gestion_projets.tools import create_bat_shortcut_windows, create_bat_shortcut_linux
from pathlib import Path
from apps.main.modules.graph_perfo_0d.main_process import process_graph_perfo_0d
from apps.main.modules.trace_conv.trace_conv import launch_trace_conv
from apps.main.utils.stats import inc_views_stat

import time

def graph_perfo_0d(request, etat_id):

    data = {}
    etat = get_object_or_404(Etat, id=etat_id)

    cache_path = etat.get_cache_filepath()
    t2 = time.perf_counter()

    # if not os.path.exists(cache_path):
    # data = process_graph_perfo_0d(etat, data, cache_path)

    # else:
    # with open(cache_path, "r", encoding="utf-8") as f:
    # data_json = json.load(f)
    # data.update(data_json)

    data = process_graph_perfo_0d(etat, data, cache_path)
    t3 = time.perf_counter()

    data["etat"] = etat
    data["projet"] = etat.projet
    data["plan_amont"] = etat.plan_amont_selected
    data["plan_aval"] = etat.plan_aval_selected
    data["selected_cases"] = Cas.objects.filter(
        iso_vitesse__etat=etat,
        select=True
    )
    t4 = time.perf_counter()

    inc_views_stat("graph_perfo_0d", request.user)

    response = render(request, "trunks/main/graph_perfo0d.html", data)
    t6 = time.perf_counter()

    print("------ TIMING graph_perfo_0d ------")
    print("process_graph:", round(t3 - t2, 3), "s")
    print("finalisation:", round(t4 - t3, 3), "s")
    print("TOTAL:", round(t6 - t2, 3), "s")
    print("------------------------------------")

    return response



@require_http_methods(["POST"])
def launch_genepi_auto_from_perfo(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)

    lst_cas_selected = Cas.objects.filter(select=True, iso_vitesse__etat=etat_id)

    def parse_field(text):
        return [v.strip() for v in text.split(',') if v.strip()]

    param_genepi = {"titre": request.POST.get("titre"),
                    "ExportPDF": 'ExportPDF' in request.POST,
                    "ExportExcel": 'ExportExcel' in request.POST,
                    "ExportPPT": 'ExportPPT' in request.POST,
                    "mise_en_forme": request.POST.get("mise_en_forme"),
                    "RecalageKD": 'RecalageKD' in request.POST,
                    "TrierIso": 'TrierIso' in request.POST,
                    "DetectionCasProcheBSAM": 'DetectionCasProcheBSAM' in request.POST,
                    "Mode_Champs": 'Mode_Champs' in request.POST,
                    "dico_aubes": {
                        'Total': parse_field(
                            request.POST.get('total_aubes', '')),
                        'Primaire': parse_field(
                            request.POST.get('primaire_aubes', '')),
                        'Secondaire': parse_field(
                            request.POST.get('secondaire_aubes', '')),
                    }}

    genepi_auto_dir = Path(etat.work_directory) / "GenepiAuto"
    genepi_auto_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(genepi_auto_dir, 0o777)

    create_genepi_file(etat, lst_cas_selected, param_genepi)
    if PATH_STYLE == "windows":
        create_bat_shortcut_windows(etat, request.user)
    else:
        create_bat_shortcut_linux(etat, request.user)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': 'Fichier GENEPI créé avec succès',
            'redirect_url': reverse('graph_perfo_0d', kwargs={'etat_id': etat.id})  # Optionnel
        })

    inc_views_stat("launch_genepi_auto_from_perfo", request.user)
    return redirect("graph_perfo_0d", etat_id=etat.id)


@require_http_methods(["POST"])
def trace_conv(request, etat_id):

    etat = get_object_or_404(Etat, id=etat_id)
    lst_cas_selected = Cas.objects.filter(select=True, iso_vitesse__etat=etat_id)

    messages = []

    for case in lst_cas_selected:
        ok = launch_trace_conv(etat, case)

        if ok:
            msg = f"{case.name} : PDF TraceConv généré"
        else:
            msg = f"{case.name} : Erreur lors de la génération"

        messages.append({
            "ok": ok,
            "message": msg,
        })

    inc_views_stat("trace_conv", request.user)
    return JsonResponse({
        "messages": messages,
    })


@require_http_methods(["GET"])
def affichage_modal_create_revue_veine_from_perfo0D(request, etat_id):
    if request.headers.get('x-requested-with') != 'XMLHttpRequest':
        return HttpResponseBadRequest("Invalid request")

    lst_revue_veine = RevueVeine.objects.filter(created_by=request.user)

    return render(request, 'trunks/partials/_modal_revue_veine.html', {
        'lst_revue_veine': lst_revue_veine,
        'etat_id': etat_id,
    })
