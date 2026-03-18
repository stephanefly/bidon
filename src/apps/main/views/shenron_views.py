from pathlib import Path
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from config.settings.base import PATH_STYLE
from apps.main.forms import ProjetShenronForm
from apps.main.models import ProjetShenron
from apps.main.utils.paths import get_user_path
from apps.main.modules.genepi.create_genepi_file_for_shenron import generate_shenron_file
from apps.main.modules.gestion_projets.tools import move_cannelle_auto_file, create_cannelle_bat_shortcut_windows, create_cannelle_bat_shortcut_linux

def lst_projets_shenron(request):
    if request.method == "POST":
        form = ProjetShenronForm(request.POST)
        if form.is_valid():
            projet_shenron = form.save(commit=False)
            projet_shenron.created_by = request.user.username

            work_directory = Path(get_user_path(projet_shenron)) / "Projet_Shenron" / projet_shenron.name
            work_directory.mkdir(parents=True, exist_ok=True)

            projet_shenron.work_directory = str(work_directory)
            projet_shenron.save()

            messages.success(request, "Projet Shenron créé avec succès.")
            return redirect("lst_projets_shenron")
    else:
        form = ProjetShenronForm()

    lst_projets = ProjetShenron.objects.filter(created_by=request.user.username).order_by("-id")

    return render(
        request,
        "trunks/main/lst_projet_shenron.html",
        {
            "lst_projets_shenron": lst_projets,
            "form": form,
        },
    )


def info_projet_shenron(request, projet_shenron_id):
    projet_shenron = get_object_or_404(ProjetShenron, id=projet_shenron_id)

    blades_data = projet_shenron.blades_data if projet_shenron.blades_data else []

    return render(
        request,
        "trunks/main/info_projet_shenron.html",
        {
            "projet_shenron": projet_shenron,
            "blades_data": blades_data,
        },
    )


def save_projet_shenron(request, projet_shenron_id):
    projet = get_object_or_404(ProjetShenron, id=projet_shenron_id)

    if request.method != "POST":
        return redirect("info_projet_shenron", projet_shenron_id=projet.id)

    # =========================
    # Récupération robuste des blades
    # =========================
    blades = []
    indexes = set()

    for key in request.POST.keys():
        if key.startswith("blades["):
            try:
                index = key.split("[")[1].split("]")[0]
                indexes.add(index)
            except Exception:
                pass

    for index in sorted(indexes, key=lambda x: int(x) if str(x).isdigit() else x):
        blade = {
            "row_index": request.POST.get(f"blades[{index}][row_index]", "").strip(),
            "project": request.POST.get(f"blades[{index}][project]", "").strip(),
            "version": request.POST.get(f"blades[{index}][version]", "").strip(),
            "aube": request.POST.get(f"blades[{index}][aube]", "").strip(),
            "coupe": request.POST.get(f"blades[{index}][coupe]", "").strip(),
            "blade_index": request.POST.get(f"blades[{index}][blade_index]", "").strip(),
            "xemp": request.POST.get(f"blades[{index}][xemp]", "").strip(),
            "azimuth": request.POST.get(f"blades[{index}][azimuth]", "").strip(),
            "calage": request.POST.get(f"blades[{index}][calage]", "").strip(),
        }

        has_data = any(
            value for key, value in blade.items()
            if key != "row_index"
        )

        if has_data or blade["row_index"]:
            blades.append(blade)

    # =========================
    # Paramètres du cas
    # =========================
    projet.case_name = request.POST.get("case_name", "").strip()
    projet.case_path = request.POST.get("case_path", "").strip()
    projet.bsam_file = request.POST.get("bsam_file", "").strip()

    # =========================
    # Configuration
    # =========================
    projet.cannelle_template = request.POST.get("cannelle_template", "CO8P-ARTEMIS-MXCR").strip()
    projet.cannelle_input = request.POST.get("cannelle_input", "").strip()
    projet.xml_path = request.POST.get("xml_path", "").strip()

    projet.plan_inlet_outlet_auto = "plan_inlet_outlet_auto" in request.POST
    projet.plan_inlet = request.POST.get("plan_inlet", "").strip()
    projet.plan_outlet = request.POST.get("plan_outlet", "").strip()
    projet.plan_outlet_secondary = request.POST.get("plan_outlet_secondary", "").strip()
    projet.bec_xr_file = request.POST.get("bec_xr_file", "").strip()

    projet.blades_data = blades

    # =========================
    # Maillage
    # =========================
    projet.mesh_input = request.POST.get("mesh_input", "").strip()
    projet.batch_mode = "batch_mode" in request.POST

    # =========================
    # Paramètres numériques
    # =========================
    projet.accel_multi = request.POST.get("accel_multi", "Outpres").strip()
    projet.condition_limite = "condition_limite" in request.POST
    projet.bc_out_type = request.POST.get("bc_out_type", "Outpres").strip()
    projet.rafal_cas = "rafal_cas" in request.POST

    # =========================
    # Extraction
    # =========================
    projet.post_script = request.POST.get("post_script", "").strip()
    projet.visu_enable = "visu_enable" in request.POST
    projet.visu_script = request.POST.get("visu_script", "").strip()

    # =========================
    # Co-processing
    # =========================
    projet.conv_stop = "conv_stop" in request.POST
    projet.grid_label = request.POST.get("grid_label", "").strip()
    projet.target_param = request.POST.get("target_param", "qcorr_ref").strip()
    projet.perf_up = request.POST.get("perf_up", "Inlet").strip()
    projet.perf_down = request.POST.get("perf_down", "Outlet").strip()
    projet.copro_script = request.POST.get("copro_script", "").strip()
    projet.copro_enable = "copro_enable" in request.POST
    projet.copro_user = request.POST.get("copro_user", "").strip()

    # =========================
    # Calcul
    # =========================
    try:
        projet.iter_case = int(request.POST.get("iter_case", 3000))
    except ValueError:
        projet.iter_case = 3000

    projet.platform = request.POST.get("platform", "XANTHE").strip()

    try:
        projet.nprocs = int(request.POST.get("nprocs", 28))
    except ValueError:
        projet.nprocs = 28

    projet.elsa_version = request.POST.get("elsa_version", "v5.2.03").strip()
    projet.submit_calc = "submit_calc" in request.POST

    projet.save()

    messages.success(request, "Projet Shenron sauvegardé avec succès.")
    return redirect("info_projet_shenron", projet_shenron_id=projet.id)


def delete_projet_shenron(request, projet_sheron_id):
    projet_sheron = get_object_or_404(ProjetShenron, id=projet_sheron_id)
    projet_sheron.delete()
    messages.success(request, "Projet Shenron supprimé.")
    return redirect("lst_projets_shenron")


def rename_projet_shenron(request, projet_sheron_id):
    projet = get_object_or_404(ProjetShenron, id=projet_sheron_id)

    if request.method != "POST":
        return redirect("lst_projets_shenron")

    old_name = projet.name
    old_dir = Path(projet.work_directory) if projet.work_directory else None

    new_name = (request.POST.get("new_name") or "").strip()
    new_work_dir = (request.POST.get("new_work_dir") or "").strip()

    if not new_name and not new_work_dir:
        messages.info(request, "Aucune modification.")
        return redirect("lst_projets_shenron")

    try:
        if new_work_dir:
            target_dir = Path(new_work_dir)

            if old_dir and old_dir.exists():
                if target_dir.exists() and target_dir.resolve() != old_dir.resolve():
                    messages.error(request, "Le dossier cible existe déjà.")
                    return redirect("lst_projets_shenron")

                old_dir.rename(target_dir)
            else:
                target_dir.mkdir(parents=True, exist_ok=True)

            projet.work_directory = str(target_dir)

        elif new_name and old_dir:
            target_dir = old_dir.parent / new_name

            if old_dir.exists():
                if target_dir.exists():
                    messages.error(request, "Le dossier cible existe déjà.")
                    return redirect("lst_projets_shenron")

                old_dir.rename(target_dir)
                projet.work_directory = str(target_dir)
            else:
                messages.warning(request, "Dossier introuvable, renommage base de données uniquement.")

        if new_name:
            projet.name = new_name

        projet.save()
        messages.success(request, f"Projet Shenron mis à jour : {old_name} → {projet.name}")
        return redirect("lst_projets_shenron")

    except Exception as e:
        messages.error(request, f"Erreur lors de la mise à jour : {e}")
        return redirect("lst_projets_shenron")


def generer_shenron_script(request, projet_shenron_id):
    projet = get_object_or_404(ProjetShenron, id=projet_shenron_id)

    generate_shenron_file(request, projet)
    move_cannelle_auto_file(projet)
    if PATH_STYLE == "windows":
        create_cannelle_bat_shortcut_windows(projet, request.user)
    else:
        create_cannelle_bat_shortcut_linux(projet, request.user)

    return redirect("info_projet_shenron", projet_shenron_id=projet.id)