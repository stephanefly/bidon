import os

from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from apps.main.utils.paths import normalize_path_os, clean_user_ihm_path
from apps.main.forms import RevueVeineForm
from apps.main.models import Cas, Etat, IsoVitesse, RevueVeine
from apps.main.modules.bsam.bsam_tools import make_veine_plot, bsam_file_test
from apps.main.modules.gestion_projets.tools import load_carac_config
from apps.main.modules.bsam.revu_veine_html_page import (
    export_excel_revue_veine,
    generate_full_data,
)
import shutil

from apps.main.utils.user_data import user_permission
import json
from pathlib import Path
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from apps.main.utils.stats import inc_views_stat
from apps.main.modules.gestion_projets.gestion_projet import duplicate_contenue_revue_veine

from apps.main.utils.paths import get_user_path
from apps.main.modules.gestion_projets.tools import (
    get_color_list,
    get_symbol_list,
)


def lst_revue_veine(request):
    lst_revue_veine = RevueVeine.objects.filter(created_by=request.user)
    form = RevueVeineForm()

    return render(
        request,
        "trunks/main/lst_revue_veine.html",
        {
            "lst_revue_veine": lst_revue_veine,
            "form": form,
        },
    )


@require_http_methods(["POST"])
def add_revue_veine(request):
    form = RevueVeineForm(request.POST)

    if form.is_valid():
        name = form.cleaned_data["name"]

        if RevueVeine.objects.filter(name=name,
                                     created_by=request.user).exists():
            messages.error(request, "Une Revue existe déjà avec ce nom !")
        else:
            revue = form.save(commit=False)
            revue.created_by = request.user
            revue.work_directory = Path(
                get_user_path(revue)) / "RevueVeine" / revue.name
            revue.work_directory.mkdir(parents=True, exist_ok=True)
            revue.save()
            os.chmod(revue.work_directory, 0o777)
            messages.success(request, f"{revue.name} créée")

    return redirect("lst_revue_veine")


def info_revue_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)
    cas_list = Cas.objects.filter(revue_veine=revue_veine)

    lst_carac_default = load_carac_config(3)

    return render(
        request,
        "trunks/main/info_revue_veine.html",
        {
            "revue_veine": revue_veine,
            "cas_list": cas_list,
            "color_options": get_color_list(),
            "symbol_options": get_symbol_list(),
            "lst_carac": lst_carac_default
        },
    )


@require_http_methods(["POST"])
def create_new_revue_veine(request):
    etat_id = request.POST.get("etat_id")
    etat = get_object_or_404(Etat, id=etat_id)

    # Cas sélectionnés
    try:
        cases_ids = json.loads(request.POST.get("cases_ids", "[]"))
        cases_ids = [int(c) for c in cases_ids if str(c).isdigit()]
    except Exception:
        cases_ids = []

    revue_id = (request.POST.get("revue_id") or "").strip()
    name = (request.POST.get("name") or "").strip()

    is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"

    # -------------------------
    # 1) Récupérer / Créer revue
    # -------------------------
    if revue_id:
        revue_veine = get_object_or_404(RevueVeine, id=revue_id, created_by=request.user)
        created = False
    else:
        form = RevueVeineForm(request.POST)
        if not form.is_valid():
            return JsonResponse({"success": False, "error": "Nom de revue invalide."}, status=400)

        if RevueVeine.objects.filter(name=name, created_by=request.user).exists():
            return JsonResponse({"success": False, "error": "Une revue avec ce nom existe déjà !"}, status=400)

        revue_veine = form.save(commit=False)
        revue_veine.created_by = request.user

        # Prépare workdir AVANT save => 1 seul save
        workdir = Path(get_user_path(revue_veine)) / "Revue_Veine" / revue_veine.name
        workdir.mkdir(parents=True, exist_ok=True)
        revue_veine.work_directory = str(workdir)

        revue_veine.save()
        os.chmod(revue_veine.work_directory, 0o777)
        created = True

    # -------------------------
    # 2) Associer les cas
    # -------------------------
    if cases_ids:
        Cas.objects.filter(
            id__in=cases_ids,
            iso_vitesse__etat=etat
        ).update(revue_veine=revue_veine)

    # -------------------------
    # 3) Réponse unique (AJAX ou non)
    # -------------------------
    redirect_url = reverse("info_revue_veine", kwargs={"revue_veine_id": revue_veine.id})
    message = f"{revue_veine.name} : Revue Veine {'créée' if created else 'associée'}"

    if is_ajax:
        return JsonResponse({
            "success": True,
            "redirect_url": redirect_url,
            "message": message
        })

    return redirect("info_revue_veine", revue_veine_id=revue_veine.id)


def delete_revue_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)
    revue_veine_name = revue_veine.name
    if str(request.user) == revue_veine.created_by:
        shutil.rmtree(revue_veine.work_directory)
        revue_veine.delete()
        messages.info(request, f"{revue_veine_name} : Revue Veine supprimé")
    return redirect("lst_revue_veine")



def rename_revue_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)

    old_name = revue_veine.name
    new_name = (request.POST.get("new_name") or "").strip()

    if not new_name:
        messages.error(request, "Nom invalide.")
        return redirect("lst_revue_veine")

    # Vérifie l'unicité pour l'utilisateur
    if RevueVeine.objects.filter(
        name=new_name,
        created_by=str(request.user)
    ).exclude(id=revue_veine_id).exists():
        messages.error(request, f"{old_name} : Le nom est déjà existant !")
        return redirect("lst_revue_veine")

    old_dir = Path(revue_veine.work_directory)
    new_dir = old_dir.parent / new_name

    try:
        # Renommage du dossier si existant
        if old_dir.exists():
            if new_dir.exists():
                messages.error(request, f"{old_name} : Le dossier est déjà existant")
                return redirect("lst_revue_veine")

            old_dir.rename(new_dir)
        else:
            messages.warning(
                request,
                "Dossier de travail introuvable, renommage base de données uniquement."
            )

        # Renommage métier (ta méthode)
        revue_veine.rename(new_name)

        # Mise à jour du work_directory
        revue_veine.work_directory = str(new_dir)
        revue_veine.save(update_fields=["work_directory"])

        messages.info(
            request,
            f"La Revue a été renommée : {old_name} → {new_name}"
        )

    except Exception as e:
        messages.error(request, f"Erreur lors du renommage : {e}")

    return redirect("lst_revue_veine")


def duplicate_revue_veine(request, revue_veine_id):
    new_name = request.POST.get("new_name")
    old_revue = get_object_or_404(RevueVeine, id=revue_veine_id)

    duplicate_contenue_revue_veine(request, new_name, old_revue)
    return redirect("lst_revue_veine")


def download_pdf_trace_veine(request, revue_veine_id):
    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)

    image_path = make_veine_plot(revue_veine)
    message_data = f"{os.path.basename(image_path)} : Généré"
    inc_views_stat("trace_veine", request.user)
    return JsonResponse({"ok": True, "message_data": message_data})

@require_http_methods(["POST"])
def ajouter_bsam(request, revue_veine_id):

    raw = request.POST.get("bsam_path", "")
    raw_path = clean_user_ihm_path(raw)

    revue = get_object_or_404(RevueVeine, id=revue_veine_id)
    # 1) Construire le Path depuis l'input user
    p = Path(raw_path)
    file_name = p.name

    # 2) Normaliser selon l'OS / environnement (retour attendu: str ou Path)
    file_path = normalize_path_os(p)

    # 3) Travailler avec un Path "cohérent" pour dériver le dossier parent
    fp = Path(file_path)  # ok si file_path est déjà un Path ou une string
    repertory = str(fp.parent)

    if (bsam_file_test(file_path)[0]
            and user_permission(request.user.username, repertory)):

        new_iso_vitesse = IsoVitesse.objects.create(
            color="black",
            name=file_name,
            file_type="bsam",
            marker="circle",
        )

        cas = Cas.objects.create(
            file_path=str(fp),
            bsam_path=str(fp),
            name=file_name,
            repertory=repertory,
            obj_type="bsam",
            revue_veine=revue,
            iso_vitesse=new_iso_vitesse,
        )

        messages.info(request, f"{file_name} : bsam ajouté")

    else:
        messages.error(request, f"{file_name} : bsam pas ajouté")


    return redirect("info_revue_veine", revue_veine_id=revue_veine_id)


@require_http_methods(["POST"])
def export_graph_detais_bsam(request, revue_veine_id):

    revue_veine = get_object_or_404(RevueVeine, id=revue_veine_id)

    hauteurs = sorted([float(h) for h in
                [request.POST.get(f"hauteur_base_{i}") for i in range(1, 7)] if
                h])

    lst_carac = load_carac_config(len(hauteurs))

    # Appliquer les cases cochées venant du POST
    for i, carac in enumerate(lst_carac):
        carac["checked"] = (request.POST.get(f"carac_{i}") == "on")
    # Filtrer uniquement celles cochées
    carac_checked = [c for c in lst_carac if c["checked"]]

    # Génération du contenu HTML et Excel
    html_content, all_excel_data = generate_full_data(carac_checked, revue_veine, hauteurs)
    timestamp = datetime.now().strftime('%Y%m%d-%H%M')
    work_repo = Path(revue_veine.work_directory)

    # Export Excel
    export_excel_revue_veine(revue_veine, all_excel_data, timestamp, work_repo)

    # Création du HTML
    html_filename = f"RevueVeine_{revue_veine.name}_{timestamp}.html"
    html_path = work_repo / html_filename
    html_path.write_text(html_content, encoding="utf-8")

    if html_path.exists():
        message_data = f"{html_filename} : Généré"
        ok = True
    else:
        message_data = f"{html_filename} : Erreur lors de la génération "
        ok = False
    inc_views_stat("launch_revue_veine", request.user)
    return JsonResponse({"ok": ok, "message_data": message_data})


def remove_bsam(request, revue_veine_id, cas_id):
    cas = get_object_or_404(Cas, id=cas_id)
    cas_name = cas.name
    cas.revue_veine = None

    if cas.iso_vitesse.etat is None:
        cas.delete()
    else:
        cas.save()

    messages.info(request, f"{cas_name} : bsam supprimé")
    return redirect("info_revue_veine", revue_veine_id=revue_veine_id)
