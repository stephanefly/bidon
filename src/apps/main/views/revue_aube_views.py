import os
from pathlib import Path
from config.settings.base import PATH_STYLE
from django.contrib import messages
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from apps.main.forms import AubeForm, RevueAubeForm
from apps.main.models import Aube, RevueAube
from apps.main.modules.genepi.create_genepi_from_revue_aube import (
    create_py_file,
)
from apps.main.modules.gestion_projets.tools import get_color_list, move_genepi_file, create_bat_shortcut_windows, create_bat_shortcut_linux
from apps.main.utils.paths import get_user_path
from apps.main.utils.stats import inc_views_stat
from apps.main.modules.gestion_projets.gestion_projet import duplicate_contenue_revue_aube
from apps.main.utils.user_data import user_permission

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
            work_directory = Path(get_user_path(revue_aube)) / "RevueAube" / revue_aube.name
            work_directory.mkdir(parents=True, exist_ok=True)
            revue_aube.work_directory = work_directory
            os.chmod(work_directory, 0o777)
            revue_aube.save()
            messages.info(request, f"Revue Aube créée : {revue_aube.name}")
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
        messages.info(request, f"{revue_aube.name} : Revue Aube supprimé")
        revue_aube.delete()
    else:
        messages.info(request, f"Tentative suppression refusée Revue Aube id={revue_aube_id}")
    return redirect("lst_revue_aube")



def rename_revue_aube(request, revue_aube_id):
    revue_aube = get_object_or_404(RevueAube, id=revue_aube_id)

    old_name = revue_aube.name
    new_name = request.POST.get("new_name", "").strip()

    if not new_name:
        messages.error(request, "Nom invalide.")
        return redirect("lst_revue_aube")

    # Vérifie l'unicité du nom
    if RevueAube.objects.filter(name=new_name).exclude(id=revue_aube_id).exists():
        messages.error(request, "Le nom est déjà existant !")
        return redirect("lst_revue_aube")

    old_dir = Path(revue_aube.work_directory)
    new_dir = old_dir.parent / new_name

    try:
        # Vérification dossier existant
        if old_dir.exists():
            if new_dir.exists():
                messages.error(request, "Le dossier cible existe déjà.")
                return redirect("lst_revue_aube")

            old_dir.rename(new_dir)
        else:
            messages.warning(request, "Dossier de travail introuvable, renommage DB uniquement.")

        # Mise à jour modèle
        revue_aube.name = new_name
        revue_aube.work_directory = str(new_dir)
        revue_aube.save()

        messages.success(
            request,
            f"Revue renommée : {old_name} → {new_name}"
        )

    except Exception as e:
        messages.error(request, f"Erreur lors du renommage : {e}")

    return redirect("lst_revue_aube")


def info_revue_aube(request, revue_aube_id):
    revue_aube = get_object_or_404(RevueAube, pk=revue_aube_id)
    lst_aube = Aube.objects.filter(revue_aube_id=revue_aube_id).order_by("id")

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

    form = AubeForm(request.POST)
    if form.is_valid() and user_permission(request.user.username, form.clean_fichier_bsam):
        aube = form.save(commit=False)
        aube.revue_aube = revue_aube
        aube.save()
        messages.info(request, f"Aube créée")
        return redirect("info_revue_aube", revue_aube_id=revue_aube.id)

    messages.error(request, "Veuillez corriger les erreurs du formulaire.")
    # si erreurs, on réaffiche la page avec le modal ouvert et le form en erreur
    lst_aube = Aube.objects.filter(revue_aube_id=revue_aube_id).order_by("id")

    return render(
        request,
        "trunks/main/info_revue_aube.html",
        {
            "revue_aube": revue_aube,
            "lst_aube": lst_aube,
            "form": form,
            "open_modal": True,  # pour auto-ouvrir le modal si erreurs
            "dico_genepi_auto": os.path.basename(revue_aube.dico_genepi_auto),
            "color_options": get_color_list(),
        },
    )


@require_http_methods(["POST"])
def aube_update(request, revue_aube_id, aube_id):
    revue = get_object_or_404(RevueAube, pk=revue_aube_id)
    aube = get_object_or_404(Aube, pk=aube_id)
    form = AubeForm(request.POST, request.FILES, instance=aube)

    if form.is_valid():
        updated_aube = form.save(commit=False)

        # Préserver la valeur originale de `used`
        updated_aube.used = aube.used

        # Rattachement explicite à la revue
        updated_aube.revue_aube = revue

        updated_aube.save()
        messages.info(request, f"Aube mise à jour")
    else:
        messages.info(request, f"Erreur formulaire update Aube id={aube_id} dans Revue id={revue_aube_id}")

    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)


def aube_delete(request, revue_aube_id, aube_id):
    aube = get_object_or_404(Aube, pk=aube_id)
    messages.info(request, f"Suppression Aube")
    aube.delete()
    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)


@require_http_methods(["POST"])
def aube_duplicate(request, revue_aube_id, aube_id):
    aube = get_object_or_404(Aube, pk=aube_id)
    # on duplique sans l'ID (pk)
    aube.pk = None
    aube.id = None
    aube.save()

    messages.info(request, f"Aube dupliquée")
    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)


@require_http_methods(["POST"])
def launch_revue_aube(request, revue_aube_id):
    revue_aube = get_object_or_404(RevueAube, id=revue_aube_id)

    lst_aubes = Aube.objects.filter(revue_aube=revue_aube, used=True)

    move_genepi_file(revue_aube,)
    create_py_file(revue_aube, lst_aubes, request.user)
    if PATH_STYLE == "windows":
        create_bat_shortcut_windows(revue_aube, request.user)
    else:
        create_bat_shortcut_linux(revue_aube, request.user)

    # 3) Si tout est ok
    messages.info(request, "Génération terminée.")

    inc_views_stat("launch_revue_aube", request.user)
    return redirect("info_revue_aube", revue_aube_id=revue_aube_id)



@require_http_methods(["POST"])
def active_aube(request, revue_aube_id, aube_id):
    aube = get_object_or_404(Aube, id=aube_id)
    aube.used = not aube.used  # Inverse la valeur de used
    aube.save()

    return JsonResponse({"success": True, "aube_name" : aube.aube, "used": aube.used})


def afficher_code_dico(request, pk):
    revue_aube = get_object_or_404(RevueAube, pk=pk)

    file_path = revue_aube.dico_genepi_auto
    file_name = os.path.basename(file_path)
    messages.info(request, f"Affichage dico : {file_name}")

    try:
        with open(file_path, encoding="utf-8") as f:
            code_content = f.read()
    except:
        file_path_local = os.path.join("src", file_path)
        with open(file_path_local, encoding="utf-8") as f:
            code_content = f.read()

    return render(
        request,
        "trunks/main/view_dico.html",
        {"code": code_content, "filename": file_name, "path": file_path},
    )


def telecharger_code_dico(request, pk):
    revue_aube = get_object_or_404(RevueAube, pk=pk)

    file_path = revue_aube.dico_genepi_auto
    file_name = os.path.basename(file_path)

    try:
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    except:
        file_path_local = os.path.join("src", file_path)
        # Retourne le fichier en téléchargement
        response = FileResponse(open(file_path_local, 'rb'), as_attachment=True)

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'
    return response


def changer_dico(request, pk):
    revue_aube = get_object_or_404(RevueAube, pk=pk)

    if request.method == "POST" and request.FILES.get("new_file"):
        uploaded_file = request.FILES["new_file"]
        messages.info(request, f"Nouveau dico upload : {uploaded_file.name}")

        # Dossier cible = work_directory de l’objet
        work_directory = Path(revue_aube.work_directory)
        work_directory.mkdir(parents=True, exist_ok=True)

        # Nouveau chemin du fichier
        new_path = os.path.join(work_directory, uploaded_file.name)

        # Sauvegarde du fichier
        with open(new_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Mise à jour du champ modèle si tu veux qu’il référence le nouveau fichier
        revue_aube.dico_genepi_auto = new_path
        revue_aube.save()

    elif request.method == "POST":
        messages.info(request, "Changement dico demandé, mais aucun fichier n'a été fourni.")

    return redirect("info_revue_aube", revue_aube_id=revue_aube.id)


def duplicate_revue_aube(request, revue_aube_id):
    new_name = request.POST.get("new_name")
    old_revue = get_object_or_404(RevueAube, id=revue_aube_id)

    duplicate_contenue_revue_aube(request, new_name, old_revue)
    return redirect("lst_revue_aube")

