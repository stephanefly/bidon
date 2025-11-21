import os
from datetime import datetime
from apps.main.modules.gestion_projets.tools import get_user_path, get_color_list, get_symbol_list
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from apps.main.forms import RevueVeineForm
from django.http import JsonResponse
import json
from apps.main.models import Cas, RevueVeine, Etat, IsoVitesse
from apps.main.modules.bsam.bsam_tools import make_veine_plot
from apps.main.modules.bsam.bsam_tools import load_carac_config
from apps.main.modules.bsam.generate_veine_pdf import generate_pdf_trace_veine
from apps.main.modules.bsam.revu_veine_html_page import generate_full_data, export_excel_revue_veine
from django.shortcuts import redirect, get_object_or_404

def get_image(request, revue_veine_id):
    output_dir = os.path.join(etat.work_directory, "ConvAuto")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)
    file_path = revue_veine.get_image_path()
    if os.path.exists(file_path):
        return FileResponse(open(file_path, "rb"), content_type="image/png")


def info_revue_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)
    cas_list = Cas.objects.filter(revue_veine=revue_veine)

    return render(
        request,
        "trunks/main/info_revue_veine.html",
        {
            "revue_veine": revue_veine,
            "cas_list": cas_list,
            "color_options": get_color_list(),
            "symbol_options": get_symbol_list(),
        },
    )


@require_http_methods(["POST"])
def create_new_revue_veine(request):
    import json

    etat_id = request.POST.get("etat_id")
    etat = get_object_or_404(Etat, id=etat_id)

    # Récupération sécure des cas sélectionnés
    cases_ids_json = request.POST.get("cases_ids", "[]")
    try:
        cases_ids = json.loads(cases_ids_json)
        cases_ids = [int(c) for c in cases_ids if str(c).isdigit()]
    except Exception:
        cases_ids = []

    revue_id = request.POST.get("revue_id") or ""
    name = request.POST.get("name") or ""

    # Cas 1 : associer à une revue existante
    if revue_id:
        try:
            revue_veine = RevueVeine.objects.get(id=revue_id)
        except RevueVeine.DoesNotExist:
            return JsonResponse({'error': "Revue inexistante."}, status=400)
    else:
        # Cas 2 : créer nouvelle revue
        form = RevueVeineForm(request.POST)
        if not form.is_valid():
            return JsonResponse({'error': "Nom de revue invalide."}, status=400)
        if RevueVeine.objects.filter(name=name,
                                     created_by=request.user.username).exists():
            return JsonResponse(
                {'error': "Une revue avec ce nom existe déjà !"}, status=400)

        revue_veine = form.save(commit=False)
        revue_veine.created_by = request.user.username
        revue_veine.save()

        folder_name = f"RevueVeine_{revue_veine.id}_{revue_veine.name}"
        revue_veine.directory = os.path.join(get_user_path(revue_veine),
                                             folder_name)
        revue_veine.save()

        os.makedirs(revue_veine.directory, exist_ok=True)

    # Association des cas sélectionnés
    if cases_ids:
        Cas.objects.filter(id__in=cases_ids, iso_vitesse__etat=etat).update(revue_veine=revue_veine)

    return JsonResponse({
        'success': True,
        'redirect_url': reverse('info_revue_veine', args=[revue_veine.id])
    })


def delete_revue_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)
    if str(request.user) == revue_veine.created_by:
        revue_veine.delete()
    return redirect("lst_revue_veine")


def rename_revue_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)
    name = request.POST.get("new_name")
    if not RevueVeine.objects.filter(name=name).exists():  # Vérifie l'unicité
        revue_veine.name = name
        revue_veine.save()
        messages.success(request, "La Revue a été renommé avec succès !")
    else:
        messages.error(request, "Le nom est déjà existant !")
    return redirect("lst_revue_veine")


def download_pdf_trace_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)

    image_path = make_veine_plot(revue_veine)
    response = generate_pdf_trace_veine(image_path, revue_veine)

    return response


def ajouter_bsam(request, revue_veine_id):
    if request.method == 'POST':
        bsam_path = request.POST.get('bsam_path')
        raw_path = request.POST.get('bsam_path', '').strip()
        path = raw_path.strip('"')  # Nettoyage ici
        revue = get_object_or_404(RevueVeine, id=revue_veine_id)
        if bsam_path:
            new_iso_vitesse = IsoVitesse.objects.create(
                color="black",
                name=os.path.basename(path),
                file_type="bsam",
                marker='circle',
            )
            new_cas = Cas.objects.create(
                file_path=path,
                bsam_path=path,
                name=os.path.basename(path),
                repertory=os.path.dirname(path),
                obj_type="bsam",
                revue_veine=revue,
                iso_vitesse=new_iso_vitesse
            )

    return redirect('info_revue_veine', revue_veine_id=revue_veine_id)


@require_http_methods(["GET", "POST"])
def export_graph_detais_bsam(request, revue_veine_id):

    lst_cas = Cas.objects.filter(revue_veine=revue_veine_id, used=True)

    if lst_cas.exists():

        revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)

        hauteurs = sorted([float(h) for h in
                    [request.POST.get(f"hauteur_base_{i}") for i in range(1, 7)] if
                    h])

        lst_carac = load_carac_config(len(hauteurs))

        # Génération du contenu HTML
        html_content, all_excel_data = generate_full_data(lst_carac,revue_veine, hauteurs)
        export_excel_revue_veine(revue_veine, all_excel_data)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Création de la réponse HTTP avec téléchargement du fichier
        response = HttpResponse(html_content, content_type="text/html")
        response[
            'Content-Disposition'] = f'attachment; filename="RevueVeine_{revue_veine.name}_{timestamp}.html"'

        return response

    else:
        messages.warning(request, "Aucun BSAM actif !")
        return redirect("info_revue_veine", revue_veine_id=revue_veine_id)


def remove_bsam(request, revue_veine_id, cas_id):
    cas = get_object_or_404(Cas, id=cas_id)

    cas.revue_veine = None

    if not hasattr(cas, 'iso_vitesse') or cas.iso_vitesse is None:
        cas.delete()
    else:
        cas.save()

    return redirect("info_revue_veine", revue_veine_id=revue_veine_id)