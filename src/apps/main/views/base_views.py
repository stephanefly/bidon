import os
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Q
from apps.main.forms import ProjectForm, RevueVeineForm
from apps.main.models import (Etat, Project, RevueVeine, IsoVitesse,
                              Cas, RevueAube, ProjetShenron)
from apps.main.modules.gestion_projets.tools import get_user_path

@login_required
def accueil(request):
    lst_projets = Project.objects.filter(created_by=request.user).order_by('etat__updated_at')[:10]
    lst_revue = RevueVeine.objects.filter(created_by=request.user).order_by('-created_at')[:10]

    return render(request, "trunks/main/accueil.html", {
        "lst_projets": lst_projets,
        "lst_revue": lst_revue
    })

@login_required
def configuration(request):
    return render(request, "trunks/main/configuration.html")

@login_required
def lst_projets(request):
    lst_projets = Project.objects.filter(created_by=request.user)
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        projet_existant = Project.objects.filter(
            name=form["name"], created_by=request.user
        ).exists()

        if not projet_existant:
            projet = form.save(commit=False)
            projet.created_by = request.user
            projet.work_directory = os.path.join(get_user_path(projet), projet.name)
            os.makedirs(projet.work_directory, exist_ok=True)
            projet.save()
            return redirect("lst_projets")
        else:
            messages.error(request, "Un projet avec ce nom existe déjà !")

    return render(
        request,
        "trunks/main/lst_projets.html",
        {"lst_projets": lst_projets, "form": form},
    )


@login_required
def lst_revue_veine(request):
    lst_revue_veine = RevueVeine.objects.filter(created_by=request.user)

    form = RevueVeineForm()

    if request.method == "POST":
        form = RevueVeineForm(request.POST)
        revue_veine_existant = RevueVeine.objects.filter(
            name=form["name"], created_by=request.user
        ).exists()

        if not revue_veine_existant:
            revue_veine = form.save(commit=False)
            revue_veine.created_by = request.user
            revue_veine.directory = os.path.join(get_user_path(revue_veine), revue_veine.name)
            os.makedirs(revue_veine.directory, exist_ok=True)
            revue_veine.save()
            return redirect("lst_revue_veine")
        else:
            messages.error(request, "Une Revue avec ce nom existe déjà !")

    return render(
        request,
        "trunks/main/lst_revue_veine.html",
        {"lst_revue_veine": lst_revue_veine, "form": form},
    )

@login_required
def recherche_globale(request):
    query = request.GET.get("q", "")
    results = {
        'projects': [],
        'etats': [],
        'cas': [],
        'iso_vitesse': [],
    }

    if query:
        results['projects'] = Project.objects.filter(Q(name__icontains=query) | Q(created_by__icontains=query))
        results['etats'] = Etat.objects.filter(name__icontains=query)
        results['cas'] = Cas.objects.filter(name__icontains=query)
        results['iso_vitesse'] = IsoVitesse.objects.filter(name__icontains=query)

    return render(request, 'trunks/main/global_search.html', {
        'query': query,
        'results': results,
    })

@login_required
def explorer(request):
    lst_etats = Etat.objects.order_by('-updated_at')
    revues = RevueVeine.objects.order_by('-created_at')
    revues_aube = RevueAube.objects.order_by('-created_at')
    projets_shenron = ProjetShenron.objects.order_by('-created_at')

    context = {
        'lst_etats': lst_etats,
        'explore_revues': revues,
        'revues_aube': revues_aube,
        'projets_shenron': projets_shenron,
    }

    return render(request, 'trunks/main/explorer.html', context)



