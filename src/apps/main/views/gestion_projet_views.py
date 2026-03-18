import os
import shutil

from pathlib import Path
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from apps.main.models import Etat, Project
from apps.main.modules.gestion_projets.gestion_projet import duplicate_cotenue_etat

from ..forms import EtatForm


def delete_projet(request, projet_id):
    projet = get_object_or_404(Project, id=projet_id)
    projet_name = projet.name
    if str(request.user) == projet.created_by:
        projet.delete()
    messages.info(request, f"{projet_name}: Projet supprimé")
    return redirect(request.META.get("HTTP_REFERER", "/"))


def rename_projet(request, projet_id):
    projet = get_object_or_404(Project, id=projet_id)
    old_name = projet.name
    new_name = request.POST.get("new_name")
    if (
        str(request.user) == projet.created_by
        and not Etat.objects.filter(
            name=new_name, created_by=str(request.user)
        ).exists()
    ):
        projet.rename_project(new_name)
        for etat in Etat.objects.filter(projet=projet):
            etat.maj_work_directory()
        messages.info(request, f"{old_name} --> {new_name}: Projet renommé")
    else:
        messages.error(request, "Le nom du projet est déjà existant !")

    return redirect("lst_projets")


def rename_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)

    old_name = etat.name
    projet_id = etat.projet.id
    new_name = (request.POST.get("new_name") or "").strip()

    if not new_name:
        messages.error(request, "Nom invalide.")
        return redirect("info_projet", projet_id=projet_id)

    # Autorisation + unicité (comme toi)
    if str(request.user) != etat.created_by:
        messages.error(request, "Action non autorisée.")
        return redirect("info_projet", projet_id=projet_id)

    if Etat.objects.filter(name=new_name, created_by=str(request.user)).exclude(id=etat_id).exists():
        messages.error(request, "Le nom de l'état est déjà existant !")
        return redirect("info_projet", projet_id=projet_id)

    old_dir = Path(etat.work_directory)
    new_dir = old_dir.parent / new_name

    try:
        # Renommage du dossier si présent
        if old_dir.exists():
            if new_dir.exists():
                messages.error(request, "Le dossier cible existe déjà.")
                return redirect("info_projet", projet_id=projet_id)

            old_dir.rename(new_dir)
        else:
            messages.warning(request, "Dossier de travail introuvable, renommage DB uniquement.")

        # Renommage métier (ta méthode) puis mise à jour du chemin
        etat.rename(new_name)
        etat.work_directory = str(new_dir)
        etat.save(update_fields=["work_directory"])  # rename() a déjà sauvé le name chez toi ? sinon enlève update_fields

        messages.info(request, f"{old_name} --> {new_name}: Projet renommé")

    except Exception as e:
        messages.error(request, f"Erreur lors du renommage : {e}")

    return redirect("info_projet", projet_id=projet_id)



def delete_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    etat_name = etat.name
    projet_id = etat.projet.id
    if str(request.user) == etat.created_by:
        try:
            shutil.rmtree(etat.work_directory)
        except:
            pass
        etat.delete()
        messages.info(request, f"{etat_name}: Etat supprimé")
    else:
        messages.error(request, f"{etat_name}: Vous n'êtes pas autorisé à le supprimé")
    return redirect("info_projet", projet_id=projet_id)


def freeze_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet_id = etat.projet.id
    if str(request.user) == etat.created_by:
        etat.freeze = True
        etat.save()
        messages.info(request, f"{etat.name}: Etat gelé")
    else:
        messages.error(request,
                       f"{etat.name}: Vous n'êtes pas autorisé à le gelé")
    return redirect("info_projet", projet_id=projet_id)


def defreeze_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet_id = etat.projet.id
    if str(request.user) == etat.created_by:
        etat.freeze = False
        etat.save()
        messages.info(request, f"{etat.name}: Etat dégelé")
    else:
        messages.error(request,
                       f"{etat.name}: Vous n'êtes pas autorisé à le dégelé")
    return redirect("info_projet", projet_id=projet_id)


def duplicate_etat(request, etat_id):
    new_name = request.POST.get("new_name")
    old_etat = get_object_or_404(Etat, id=etat_id)

    new_etat = duplicate_cotenue_etat(request, new_name, old_etat)
    messages.info(request, ": Etat crée")
    return redirect("info_projet", new_etat.projet.id)


def info_projet(request, projet_id):
    projet = get_object_or_404(Project, id=projet_id)
    lst_etat = Etat.objects.filter(projet=projet)
    form = EtatForm()

    if request.method == "POST":
        form = EtatForm(request.POST)
        if form.is_valid():
            # Vérifier si un état avec le même nom existe déjà pour ce projet
            etat_existant = Etat.objects.filter(
                name=form.cleaned_data["name"], projet=projet
            ).exists()

            if not etat_existant:
                etat = form.save(commit=False)
                etat.projet = projet
                etat.created_by = request.user
                etat.work_directory = Path(projet.work_directory) / etat.name
                etat.work_directory.mkdir(parents=True, exist_ok=True)
                etat.save()
                os.chmod(etat.work_directory, 0o777)
                return redirect("info_projet", projet_id=projet.id)
            else:
                messages.error(
                    request, "Un état avec ce nom existe déjà pour ce projet."
                )

    data = {"projet": projet, "lst_etat": lst_etat, "form": form}
    return render(request, "trunks/main/lst_etat.html", data)
