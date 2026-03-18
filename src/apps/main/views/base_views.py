import os
from config.settings.base import PATH_STYLE
from pathlib import Path
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from apps.main.utils.paths import get_user_path
from apps.main.forms import ProjectForm, RevueVeineForm
from apps.main.models import (
    Project, Etat, Cas, IsoVitesse,
    UtilitaireConfiguration, RevueVeine,
    ProjetShenron, RevueAube, Aube,
    Row, RowPair, Stat
)
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncWeek

from django.shortcuts import render


@login_required
def accueil(request):
    lst_projets = Project.objects.filter(created_by=request.user).order_by('etat__updated_at')[:5]
    lst_revue = RevueVeine.objects.filter(created_by=request.user).order_by('-created_at')[:5]
    lst_revue_aube = RevueAube.objects.filter(created_by=request.user).order_by('-created_at')[:5]
    lst_projet_sheron = ProjetShenron.objects.filter(created_by=request.user).order_by('-created_at')[:5]



    return render(request, "trunks/main/accueil.html", {
        "lst_projets": lst_projets,
        "lst_revue": lst_revue,
        "lst_revue_aube": lst_revue_aube,
        "lst_projet_sheron": lst_projet_sheron,
        "ENVIRONNEMENT": PATH_STYLE,
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
            name=form["name"],
            created_by=request.user
        ).exists()

        if not projet_existant:
            projet = form.save(commit=False)
            projet.created_by = request.user
            projet.work_directory = Path(
                get_user_path(projet)) / "Perfos0D" / projet.name
            projet.work_directory.mkdir(parents=True, exist_ok=True)
            projet.save()
            os.chmod(projet.work_directory, 0o777)
            return redirect("lst_projets")
        else:
            messages.error(request, "Un projet avec ce nom existe déjà !")

    return render(
        request,
        "trunks/main/lst_projets.html",
        {"lst_projets": lst_projets, "form": form},
    )


@login_required
def recherche_globale(request):
    query = request.GET.get("q", "").strip()

    results = {
        "projects": Project.objects.none(),
        "etats": Etat.objects.none(),
        "cas": Cas.objects.none(),
        "iso_vitesse": IsoVitesse.objects.none(),
        "revue_veine": RevueVeine.objects.none(),
        "projets_shenron": ProjetShenron.objects.none(),
        "revues_aube": RevueAube.objects.none(),
    }

    has_results = False

    if query:
        results["projects"] = Project.objects.filter(
            Q(name__icontains=query) |
            Q(created_by__icontains=query) |
            Q(work_directory__icontains=query)
        )

        results["etats"] = Etat.objects.filter(
            Q(name__icontains=query) |
            Q(projet__name__icontains=query) |
            Q(created_by__icontains=query) |
            Q(work_directory__icontains=query)
        )

        results["cas"] = Cas.objects.filter(
            Q(name__icontains=query) |
            Q(obj_type__icontains=query) |
            Q(iso_vitesse__name__icontains=query) |
            Q(iso_vitesse__etat__name__icontains=query)
        )

        results["iso_vitesse"] = IsoVitesse.objects.filter(
            Q(name__icontains=query) |
            Q(etat__name__icontains=query) |
            Q(etat__projet__name__icontains=query)
        )

        results["revue_veine"] = RevueVeine.objects.filter(
            Q(name__icontains=query) |
            Q(created_by__icontains=query) |
            Q(work_directory__icontains=query)
        )

        results["projets_shenron"] = ProjetShenron.objects.filter(
            Q(name__icontains=query) |
            Q(created_by__icontains=query) |
            Q(work_directory__icontains=query)
        )

        results["revues_aube"] = RevueAube.objects.filter(
            Q(name__icontains=query) |
            Q(created_by__icontains=query) |
            Q(work_directory__icontains=query) |
            Q(dico_genepi_auto__icontains=query)
        )

        has_results = any(qs.exists() for qs in results.values())

    return render(
        request,
        "trunks/main/global_search.html",
        {
            "query": query,
            "results": results,
            "has_results": has_results,
        },
    )


@login_required
def explorer(request):
    lst_projets = Project.objects.order_by('-created_by')
    revues = RevueVeine.objects.order_by('-created_at')
    revues_aube = RevueAube.objects.order_by('-created_at')
    projets_shenron = ProjetShenron.objects.order_by('-created_at')

    context = {
        'lst_projets': lst_projets,
        'explore_revues': revues,
        'revues_aube': revues_aube,
        'projets_shenron': projets_shenron,
    }

    return render(request, 'trunks/main/explorer.html', context)


def news_view(request):
    return render(request, 'trunks/main/news.html')

def stats_view(request):
    # TOTAL GLOBAL (par name)
    total_stats = (
        Stat.objects
        .values("name")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    # PAR MOIS
    stats_by_month = (
        Stat.objects
        .annotate(month=TruncMonth("created_at"))
        .values("name", "month")
        .annotate(total=Count("id"))
        .order_by("month", "-total")
    )

    # PAR SEMAINE
    stats_by_week = (
        Stat.objects
        .annotate(week=TruncWeek("created_at"))
        .values("name", "week")
        .annotate(total=Count("id"))
        .order_by("week", "-total")
    )

    return render(request, "trunks/main/stats.html", {
        "total_stats": total_stats,
        "stats_by_month": stats_by_month,
        "stats_by_week": stats_by_week,
    })