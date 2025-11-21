import os
from pathlib import Path
from django.http import FileResponse, Http404, JsonResponse
from django.views.decorators.http import require_http_methods
import datetime
from apps.main.modules.gestion_projets.tools import get_user_path
from apps.main.modules.bsam.revue_aube import create_py_file, create_bat_shortcut
from django.conf import settings
from django.contrib import messages
import shutil
from apps.main.modules.gestion_projets.tools import get_user_path, get_color_list
from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from apps.main.forms import RevueAubeForm, AubeForm

from apps.main.models import Cas, RevueAube, Etat, Aube

from django.shortcuts import redirect, get_object_or_404


def lst_revue_aube(request):
    lst_revue_aube = RevueAube.objects.filter(created_by=request.user)

    form = RevueAubeForm()

    if request.method == "POST":
        form = RevueAubeForm(request.POST)
        revue_aube_existant = RevueAube.objects.filter(
            name=form["name"], created_by=request.user
        ).exists()

        if not revue_aube_existant:
            revue_aube = form.save(commit=False)
            revue_aube.created_by = request.user
            work_dir = Path(get_user_path(revue_aube)) / "Revue_Aube" / revue_aube.name
            work_dir.mkdir(parents=True, exist_ok=True)
            revue_aube.work_dir = work_dir
            revue_aube.save()
            return redirect("lst_revue_aube")
        else:
            messages.error(request, "Une Revue avec ce nom existe déjà !")

    return render(
        request,
        "trunks/main/lst_revue_aube.html",
        {"lst_revue_aube": lst_revue_aube, "form": form,},
    )


def delete_revue_aube(request, revue_aube_id):
    revue_aube = get_object_or_404(RevueAube, id=revue_aube_id)
    if str(request.user) == revue_aube.created_by:
        revue_aube.delete()
    return redirect("lst_revue_aube")


def rename_revue_aube(request, revue_aube_id):
    revue_aube = get_object_or_404(RevueAube, id=revue_aube_id)
    name = request.POST.get("new_name")
    if not RevueAube.objects.filter(name=name).exists():  # Vérifie l'unicité
        revue_aube.name = name
        revue_aube.save()
        messages.success(request, "La Revue a été renommé avec succès !")
    else:
        messages.error(request, "Le nom est déjà existant !")
    return redirect("lst_revue_aube")


def info_revue_aube(request, revue_aube_id):
    # liste + form d'ajout
    revue_aube = get_object_or_404(RevueAube, pk=revue_aube_id)
    lst_aube = Aube.objects.filter(revue_aube_id=revue_aube_id).order_by("id")
    # attache un form d'édition à chaque aube (GET uniquement)
    for a in lst_aube:
        a.edit_form = AubeForm(instance=a)
    context = {
        "revue_aube": revue_aube,
        "dico_genepi_auto": os.path.basename(revue_aube.dico_genepi_auto),
        "lst_aube": lst_aube,
        "form": AubeForm(),
        "color_options": get_color_list(),
    }
    return render(request, "trunks/main/info_revue_aube.html", context)


def aube_create(request, revue_aube_id):
    revue_aube = get_object_or_404(RevueAube, pk=revue_aube_id)

    if request.method != "POST":
        return redirect("info_revue_aube", revue_aube_id=revue_aube.id)

    form = AubeForm(request.POST)
    if form.is_valid():
        aube = form.save(commit=False)
        aube.revue_aube = revue_aube
        aube.save()
        messages.success(request, "Aube ajoutée.")
        return redirect("info_revue_aube", revue_aube_id=revue_aube.id)

    # si erreurs, on réaffiche la page avec le modal ouvert et le form en erreur
    lst_aube = revue.aubes.order_by("id")
    messages.error(request, "Veuillez corriger les erreurs du formulaire.")
    return render(request, "trunks/main/info_revue_aube.html", {
        "revue": revue,
        "lst_aube": lst_aube,
        "form": form,
        "open_modal": True,  # pour auto-ouvrir le modal si erreurs
    })


@require_http_methods(["POST"])
def aube_update(request, revue_aube_id, aube_id):
    revue = get_object_or_404(RevueAube, pk=revue_aube_id)
    aube = get_object_or_404(Aube, pk=aube_id)
    form = AubeForm(request.POST, request.FILES, instance=aube)
    if form.is_valid():
        updated_aube = form.save(commit=False)
        updated_aube.revue = revue  # rattachement explicite
        updated_aube.save()

    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)


def aube_delete(request, revue_aube_id, aube_id):
    aube = get_object_or_404(Aube, pk=aube_id)
    aube.delete()
    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)


@require_http_methods(["POST"])
def aube_duplicate(request, revue_aube_id, aube_id):
    aube = get_object_or_404(Aube, pk=aube_id)
    # on duplique sans l'ID (pk)
    aube.pk = None
    aube.id = None
    aube.save()
    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)


@require_http_methods(["POST"])
def launch_revue_aube(request, revue_aube_id):
    revue_aube = get_object_or_404(RevueAube, id=revue_aube_id)

    lst_aubes = Aube.objects.filter(revue_aube=revue_aube, used=True)

    for aube in lst_aubes:

        # --- Copier fichier_bsam ---
        src = Path(aube.fichier_bsam)
        dst = Path(revue_aube.work_dir) / src.name
        if not src == dst:
            shutil.copy2(src, dst)
            aube.fichier_bsam = str(dst)

        # --- Copier lien_xml ---
        src = Path(aube.lien_xml)
        dst = Path(revue_aube.work_dir) / src.name
        if not src == dst:
            shutil.copy2(src, dst)
            aube.lien_xml = str(dst)

        # Sauvegarde en base avec les nouveaux chemins
        aube.save()

    # --- Copier le dictionnaire ---
    src = "src" / Path(revue_aube.dico_genepi_auto)
    dst = Path(revue_aube.work_dir) / src.name
    if not src == dst:
        shutil.copy2(src, dst)
        aube.fichier_bsam = str(dst)
        revue_aube.dico_genepi_auto = os.path.join(revue_aube.work_dir, src.name)

    create_py_file(revue_aube, lst_aubes, request.user)
    create_bat_shortcut(revue_aube, request.user)

    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)


@require_http_methods(["POST"])
def active_aube(request, revue_aube_id, aube_id):
    aube = get_object_or_404(Aube, id=aube_id)
    aube.used = not aube.used  # Inverse la valeur de used
    aube.save()
    # Renvoyer un JSON avec les informations nécessaires
    return JsonResponse({"success": True, "used": aube.used})


def afficher_code_dico(request, pk):
    # Récupération de l’objet
    revue_aube = get_object_or_404(RevueAube, pk=pk)

    file_path = revue_aube.dico_genepi_auto

    # Lecture du contenu
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code_content = f.read()
    except:
        file_path_local = os.path.join("src", file_path)
        with open(file_path_local, 'r', encoding='utf-8') as f:
            code_content = f.read()

    # Affichage dans un template
    return render(request, "trunks/main/view_dico.html", {
        'code': code_content,
        'filename': os.path.basename(file_path),
        'path': file_path
    })


def telecharger_code_dico(request, pk):
    # Récupération de l’instance
    revue_aube = get_object_or_404(RevueAube, pk=pk)

    # Construction du chemin absolu
    file_path = revue_aube.dico_genepi_auto
    # Lecture du contenu
    try:
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    except:
        file_path_local = os.path.join("src", file_path)
        # Retourne le fichier en téléchargement
        response = FileResponse(open(file_path_local, 'rb'), as_attachment=True)

    response[
        'Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response


def changer_dico(request, pk):
    revue_aube = get_object_or_404(RevueAube, pk=pk)

    if request.method == "POST" and request.FILES.get("new_file"):
        uploaded_file = request.FILES["new_file"]

        # Dossier cible = work_dir de l’objet
        work_dir = revue_aube.work_dir
        os.makedirs(work_dir, exist_ok=True)

        # Nouveau chemin du fichier
        new_path = os.path.join(work_dir, uploaded_file.name)

        # Sauvegarde du fichier
        with open(new_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Mise à jour du champ modèle si tu veux qu’il référence le nouveau fichier
        revue_aube.dico_genepi_auto = new_path
        revue_aube.save()

    return redirect("info_revue_aube", revue_aube_id=revue_aube.id)
