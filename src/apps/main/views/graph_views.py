import os.path
from datetime import datetime

from django.http import FileResponse, Http404, JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.conf import settings

from apps.main.models import Cas, Etat, IsoVitesse
from apps.main.modules.genepi.create_file_genepi import (
    create_genepi_bat_file,
    create_genepi_file,
)
from apps.main.modules.trace_conv.trace_conv import launch_trace_conv
from apps.main.modules.graph_perfo_0d.main_process import process_graph_perfo_0d


def graph_perfo_0d(request, etat_id):
    data = {}
    etat = get_object_or_404(Etat, id=etat_id)
    cache_path = etat.get_cache_filepath()

    # if not os.path.exists(cache_path):
    print("CALCULATING DATA")
    data = process_graph_perfo_0d(etat, data, cache_path)

    # else:
    #     print("LECTURE CACHE FILE")
    #     with open(cache_path, "r", encoding="utf-8") as f:
    #         data_json = json.load(f)
    #         data.update(data_json)

    # print(data)
    # 5. FINALISATION
    data["etat"] = etat
    data["projet"] = etat.projet
    data["selected_cases"] = Cas.objects.filter(iso_vitesse__etat=etat, select=True)

    return render(request, "trunks/main/graph_perfo0d.html", data)


@require_http_methods(["POST"])
def download_graph(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)

    html_filepath = os.path.join(etat.work_directory, f"{settings.PERFOS0D_EXPORT_NAME}.html")

    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_filename = f"Perfos0D_{etat.projet.name}_{etat.name}_{current_date}.html"
    if os.path.exists(html_filepath):
        return FileResponse(
            open(html_filepath, "rb"),
            as_attachment=True,
            filename=new_filename,
        )
    else:
        raise Http404("Fichier introuvable")


@require_http_methods(["POST"])
def action1(request, etat_id):
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
    print(param_genepi)
    try:
        if not os.path.exists(os.path.join(etat.work_directory, 'GenepiAuto')):
            os.makedirs(os.path.join(etat.work_directory, 'GenepiAuto'))

        create_genepi_file(etat, lst_cas_selected, param_genepi)
        create_genepi_bat_file(etat.work_directory, request)

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': 'Fichier GENEPI créé avec succès',
                'redirect_url': reverse('graph_perfo_0d', kwargs={'etat_id': etat.id})  # Optionnel
            })

        return redirect("graph_perfo_0d", etat_id=etat.id)

    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'error': f'Erreur lors de la création du fichier GENEPI: {str(e)}'
            })

        return redirect("graph_perfo_0d", etat_id=etat.id)


@require_http_methods(["POST"])
def trace_conv(request, etat_id):

    etat = get_object_or_404(Etat, id=etat_id)
    lst_cas_selected = Cas.objects.filter(select=True, iso_vitesse__etat=etat_id)

    for case in lst_cas_selected:
        launch_trace_conv(etat, case)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
                'success': True,
                'message': 'PDF de convergence généré avec succès',
                'redirect_url': reverse('graph_perfo_0d', kwargs={'etat_id': etat.id})
            })

    return redirect("graph_perfo_0d", etat_id=etat.id)



@require_http_methods(["GET"])
def create_revue_veine(request, etat_id):
    if request.headers.get('x-requested-with') != 'XMLHttpRequest':
        return HttpResponseBadRequest("Invalid request")

    etat = get_object_or_404(Etat, id=etat_id)
    lst_cas_etat = Cas.objects.filter(iso_vitesse__etat=etat)
    lst_revue_veine = list(
        {case.revue_veine for case in lst_cas_etat if case.revue_veine})
    lst_cas_selected = []  # Ajouter ceci pour éviter l'erreur

    return render(request, 'trunks/partials/_modal_revue_veine.html', {
        'lst_revue_veine': lst_revue_veine,
        'etat_id': etat_id,
        'lst_cas_selected': lst_cas_selected,
    })

