from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.main.forms  import ProjetShenronForm
from apps.main.models import ProjetShenron
from apps.main.modules.gestion_projets.tools import get_user_path, get_color_list

def lst_projets_shenron(request):
    # Création rapide
    if request.method == "POST":
        form = ProjetShenronForm(request.POST)
        if form.is_valid():
            projet_sheron = form.save(commit=False)
            projet_sheron.created_by = request.user.username
            work_dir = Path(get_user_path(projet_sheron)) / "Projet_Shenron" / projet_sheron.name
            work_dir.mkdir(parents=True, exist_ok=True)
            projet_sheron.work_dir = work_dir
            projet_sheron.save()
            messages.success(request, "Projet Shenron créé avec succès.")
            return redirect('lst_projets_shenron')
    else:
        form = ProjetShenronForm()

    lst_projets = ProjetShenron.objects.filter(created_by=request.user)

    return render(request, "trunks/main/lst_projet_shenron.html", {
        "lst_projets_shenron": lst_projets,
        "form": form,
    })

def delete_projet_shenron(request, projet_sheron_id):
    projet_sheron = get_object_or_404(ProjetShenron, id=projet_sheron_id)
    projet_sheron.delete()
    messages.success(request, "Projet Shenron supprimé.")
    return redirect('lst_projets_shenron')


def rename_projet_shenron(request, projet_sheron_id):
    projet_sheron = get_object_or_404(ProjetShenron, id=projet_sheron_id)

    if request.method == "POST":
        new_name = request.POST.get("new_name")
        new_work_dir = request.POST.get("new_work_dir", "").strip()

        if new_name:
            projet_sheron.name = new_name

        if new_work_dir:
            projet_sheron.work_dir = new_work_dir

        projet_sheron.save()
        messages.success(request, "Projet Shenron mis à jour.")
        return redirect('lst_projets_shenron')

    return redirect('lst_projets_shenron')

def info_projet_shenron(request, projet_shenron_id):
    projet_shenron = get_object_or_404(ProjetShenron, id=projet_shenron_id)
    return render(request, "trunks/main/info_projet_shenron.html", {"projet_shenron":projet_shenron})


def duplicate_projet_shenron(request, projet_shenron_id):
    new_name = request.POST.get("new_name")
    old_projet_shenron_id = get_object_or_404(Etat, id=projet_shenron_id)

    new_etat = Etat.objects.create(
        name=new_name,
        projet=old_etat.projet,
        created_by=str(request.user),
        work_directory=os.path.join(str(old_etat.projet.work_directory), str(new_name)),
        cas_temp_repertory=old_etat.cas_temp_repertory,
    )
    new_etat.save()
    duplicate_cotenue_etat(new_etat, old_etat)