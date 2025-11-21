import os
import shutil
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse

from ..forms import EtatForm
from apps.main.models import Etat, Project
from apps.main.modules.gestion_projets.gestion_projet import duplicate_cotenue_etat


def delete_projet(request, projet_id):
    projet = get_object_or_404(Project, id=projet_id)
    if str(request.user) == projet.created_by:
        projet.delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))


def rename_projet(request, projet_id):
    projet = get_object_or_404(Project, id=projet_id)
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
    else:
        messages.error(request, "Le nom du projet est déjà existant !")

    return redirect("lst_projets")


def rename_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet_id = etat.projet.id
    new_name = request.POST.get("new_name")
    if (
        str(request.user) == etat.created_by
        and not Etat.objects.filter(
            name=new_name, created_by=str(request.user)
        ).exists()
    ):
        etat.rename_etat(new_name)
        etat.save()
    else:
        messages.error(request, "Le nom de l'état est déjà existant !")
    return redirect("info_projet", projet_id=projet_id)


def delete_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet_id = etat.projet.id
    if str(request.user) == etat.created_by:
        shutil.rmtree(etat.work_directory)
        etat.delete()
    return redirect("info_projet", projet_id=projet_id)


def freeze_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet_id = etat.projet.id
    if str(request.user) == etat.created_by:
        etat.freeze = True
        etat.save()
    return redirect("info_projet", projet_id=projet_id)


def defreeze_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet_id = etat.projet.id
    if str(request.user) == etat.created_by:
        etat.freeze = False
        etat.save()
    return redirect("info_projet", projet_id=projet_id)


def duplicate_etat(request, etat_id):
    new_name = request.POST.get("new_name")
    old_etat = get_object_or_404(Etat, id=etat_id)

    new_etat = Etat.objects.create(
        name=new_name,
        projet=old_etat.projet,
        created_by=str(request.user),
        work_directory=os.path.join(str(old_etat.projet.work_directory), str(new_name)),
        cas_temp_repertory=old_etat.cas_temp_repertory,
    )
    new_etat.save()
    duplicate_cotenue_etat(new_etat, old_etat)

    return redirect("info_projet", old_etat.projet.id)


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
                etat.work_directory = os.path.join(
                    str(projet.work_directory), str(etat.name)
                )
                os.makedirs(etat.work_directory, exist_ok=True)
                etat.save()
                return redirect("info_projet", projet_id=projet.id)
            else:
                messages.error(
                    request, "Un état avec ce nom existe déjà pour ce projet."
                )

    data = {"projet": projet, "lst_etat": lst_etat, "form": form}
    return render(request, "trunks/main/lst_etat.html", data)
