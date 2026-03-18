import json
import os
from apps.main.utils.paths import normalize_path_os, clean_user_ihm_path
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from pathlib import Path
from django.http import FileResponse
from django.conf import settings
from apps.main.modules.bsam.bsam_tools import bsam_file_test
from apps.main.models import Aube, Cas, Etat, IsoVitesse
from apps.main.modules.gestion_projets.tools import get_color_list, get_symbol_list
from apps.main.modules.graph_perfo_0d.user_case import *
from apps.main.modules.graph_perfo_0d.gestion_data import get_hdf_moy, get_plane_configuration, extract_and_save_moy
from apps.main.utils.user_data import user_permission
import pandas as pd

# Vue pour afficher l'état et les Cas associés
def info_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet = etat.projet
    # Récupère tous les noms existants pour l'état donné
    lst_iso_vitesse = IsoVitesse.objects.filter(etat=etat).order_by('file_type')
    lst_cas = Cas.objects.filter(iso_vitesse__in=lst_iso_vitesse).order_by("id")
    all_case_used = sum(iso.used_cas() for iso in lst_iso_vitesse)
    get_plane_configuration(etat)

    bsam_list = []
    cannelle_list = []
    cas_user_list = []
    for iso in IsoVitesse.objects.filter(etat=etat).prefetch_related('cas_set'):
        premier_cas = iso.cas_set.first()
        if premier_cas:
            if premier_cas.obj_type == 'bsam':
                bsam_list.append(iso)
            elif premier_cas.obj_type == "cas_utilisateur":
                cas_user_list.append(iso)
            else:
                cannelle_list.append(iso)

    if request.method == "POST" and request.POST.getlist("selected_multiple_item"):

        try:
            selected_multiple_item = request.POST.getlist("selected_multiple_item")
            color_iso_vitesse = request.POST.get("color_iso_vitesse", "")
            symbole_iso_vitesse = request.POST.get("symbole_iso_vitesse", "")
            file_type = request.POST.get("input_file", "")
            name_isovitesse_input = request.POST.get("name_isovitesse_input", "")
            request.session['last_iso_vitesse_name_input'] = name_isovitesse_input
            name_isovitesse = request.POST.get("iso_vitess_name", "")
            request.session['last_iso_vitesse_name'] = name_isovitesse
            iso_vitesse = IsoVitesse.objects.create(
                color=color_iso_vitesse,
                etat=etat,
                name=name_isovitesse_input,
                file_type=file_type,
                marker=symbole_iso_vitesse,
            )

            for cas_name in selected_multiple_item:
                if cas_name not in Cas.objects.filter(
                        iso_vitesse__in=lst_iso_vitesse,obj_type="cas_cannelle"
                ):
                    try:
                        new_cas = Cas.objects.create(
                            name=cas_name,
                            iso_vitesse=iso_vitesse,
                            obj_type="cas_cannelle"
                        )
                        new_cas.set_repertory_path()

                        new_cas.get_bsam_file()
                        new_cas.save()

                        if file_type == "hdf":
                            # ATTENTION IL FAUT RECUPERER LES PLANS SELCTIONNE PAR L'UTILISATEUR !!!
                            # planes_selected = [cas.iso_vitesse.etat.plan_amont_selected,
                            #                    cas.iso_vitesse.etat.plan_aval_selected]
                            planes_selected = ['Inlet', 'Outlet']
                            new_cas.get_hdf5_path(request)
                            get_hdf_moy(new_cas, planes_selected)
                        else:
                            new_cas.get_excel_path(request)
                            str_moy = os.path.splitext(os.path.basename(new_cas.file_path))[0]
                            extract_and_save_moy(new_cas, str_moy)

                    except Exception as e:
                        messages.error(request,
                                      f"Cas non ajouté : {e}")

            if iso_vitesse.total_cas() > 0:
                messages.info(request, f"Isovitesse ajouté : {name_isovitesse_input}")
            else:
                iso_vitesse.delete()
                messages.error(request, f"Isovitesse non ajouté : {name_isovitesse_input}")
            return redirect("info_etat", etat_id=etat.id)
        except Exception as e:
            messages.error(request,
                           f"Isovitesse non ajouté : {e}")
            return redirect("info_etat", etat_id=etat.id)

    if request.method == "POST" and request.POST.getlist("selected_multiple_item2"):

        try:
            selected_multiple_item2 = request.POST.getlist("selected_multiple_item2")
            color_iso_vitesse = request.POST.get("color_iso_vitesse", "")
            symbole_iso_vitesse = request.POST.get("symbole_iso_vitesse", "")

            name_isovitesse_input2 = request.POST.get("name_isovitesse_input2", "")
            request.session['last_iso_vitesse_name_input2'] = name_isovitesse_input2
            name_isovitesse2 = request.POST.get("iso_vitess_name2", "")
            request.session['last_iso_vitesse_name2'] = name_isovitesse2

            iso_vitesse = IsoVitesse.objects.create(
                color=color_iso_vitesse,
                etat=etat,
                name=name_isovitesse_input2,
                file_type="bsam",
                marker=symbole_iso_vitesse,
            )

            for bsam_name in selected_multiple_item2:

                is_bsam, msg = bsam_file_test(os.path.join(etat.bsam_temp_repertory,
                                              bsam_name))

                if bsam_name not in Cas.objects.filter(
                        iso_vitesse__in=lst_iso_vitesse,obj_type="bsam"
                ) and is_bsam:

                    new_bsam = Cas.objects.create(
                        name=bsam_name,
                        iso_vitesse=iso_vitesse,
                        obj_type="bsam"
                    )

                    new_bsam.set_repertory_path()
                    new_bsam.get_bsam_file()
                    new_bsam.save()

                    messages.info(request,
                                  f"{bsam_name} : Bsam ajouté ")
                else:
                    messages.error(request,
                                  f" {bsam_name} : {msg} ")

            if iso_vitesse.total_cas() > 0:
                messages.info(request, f"Isovitesse ajouté : {name_isovitesse_input2}")
            else:
                iso_vitesse.delete()
                messages.error(request, f"Isovitesse non ajouté : {name_isovitesse_input2}")

            return redirect(f"{reverse('info_etat', args=[etat.id])}?tab=2")
        except Exception as e:
            messages.error(request,
                           f"Isovitesse non ajouté : {e}")
            return redirect(f"{reverse('info_etat', args=[etat.id])}?tab=2")

    if request.method == "POST" and request.POST.getlist("name_isovitesse_input3"):

        try:
            name_isovitesse_input3 = request.POST.get("name_isovitesse_input3")
            color_iso_vitesse = request.POST.get("color_iso_vitesse", "")
            symbole_iso_vitesse = request.POST.get("symbole_iso_vitesse", "")
            f = request.FILES["file_curve_data"]

            # Creation de l'isovitesse
            iso_vitesse = IsoVitesse.objects.create(
                color=color_iso_vitesse,
                etat=etat,
                name=name_isovitesse_input3,
                file_type="user_curve",
                marker=symbole_iso_vitesse,
            )

            df_file, file_path = lecture_user_file_curve(f, iso_vitesse)
            data_file = dico_listes_par_colonne(df_file, iso_vitesse, file_path)
            iso_vitesse.row_config = build_config_row(data_file)
            iso_vitesse.save()
            row_list = build_row_list(iso_vitesse.row_config)
            save_to_database(row_list, data_file, iso_vitesse)
            Cas.objects.filter(iso_vitesse=iso_vitesse).update(calculate_perfo=True)

            if iso_vitesse.total_cas() > 0:
                messages.info(request, f"Isovitesse ajouté : {name_isovitesse_input3}")
            else:
                iso_vitesse.delete()
                messages.error(request, f"Isovitesse non ajouté : {name_isovitesse_input3}")
            return redirect(f"{reverse('info_etat', args=[etat.id])}?tab=3")
        except Exception as e:
            messages.error(request,
                          f"Isovitesse non ajouté : {e}")
            return redirect(f"{reverse('info_etat', args=[etat.id])}?tab=3")

    val_name_isovitesse_input = request.session.pop('last_iso_vitesse_name_input', '')
    val_name_isovitesse = request.session.pop('last_iso_vitesse_name', '')
    val_name_isovitesse_input2 = request.session.pop('last_iso_vitesse_name_input2', '')
    val_name_isovitesse2 = request.session.pop('last_iso_vitesse_name2', '')



    return render(
        request,
        "trunks/main/info_etat.html",
        {
            "projet": projet,
            "etat": etat,
            "lst_cas": lst_cas,
            "lst_iso_vitesse": lst_iso_vitesse,
            "all_case_used": all_case_used,
            "color_options": get_color_list(),
            "symbol_options": get_symbol_list(),
            'bsam_list': bsam_list,
            'cannelle_list': cannelle_list,
            'cas_user_list' : cas_user_list,
            "val_name_isovitesse_input": val_name_isovitesse_input,
            "val_name_isovitesse" : val_name_isovitesse,
            "val_name_isovitesse_input2": val_name_isovitesse_input2,
            "val_name_isovitesse2": val_name_isovitesse2,
        },
    )


def change_item(request, model_name, item_id, action):

    MODEL_MAP = {
        "cas": Cas,
        "iso_vitesse": IsoVitesse,
        "aube": Aube,
    }

    model = MODEL_MAP.get(model_name)
    item = get_object_or_404(model, id=item_id)
    item_name = item.projet if model_name == "aube" else item.name

    if action == "active":
        item.used = not item.used
        item.calculate_perfo = False
        item.save()

        iso_vitesse = item.iso_vitesse
        used_cas = iso_vitesse.used_cas()
        total_cas = iso_vitesse.total_cas()

        return JsonResponse({
            "success": True,
            "used": item.used,
            "cas_name": item_name,
            "iso_vitesse_id": iso_vitesse.id,
            "used_cas": used_cas,
            "total_cas": total_cas,
        })

    elif action == "delete":
        cas_name = item_name
        etat_id = item.iso_vitesse.etat.id
        if len(Cas.objects.filter(iso_vitesse=item.iso_vitesse)) == 1:
            item.delete()
            item.iso_vitesse.delete()
        else:
            item.delete()

        messages.info(request, f"{cas_name} : supprimé")
        return redirect("info_etat", etat_id=etat_id)
    elif action == "update_color":
        new_color = (
                request.POST.get("color_aube")
                or request.POST.get("color_isovitesse")
                or "black"
        )
        item.color = new_color
        item.save()

        return JsonResponse({
            'success': True,
            'id': item.id,
            "message": f"{item_name} : couleur mise à jour",
        })
    elif action == "update_symbol":
        new_marker = request.POST.get(
            "symbole_isovitesse",
        )  # Défaut à noir si aucune couleur n'est sélectionnée
        item.marker = new_marker
        item.save()
        if item.etat:
            etat_id = item.etat.id
        return JsonResponse({
            'success': True,
            'id': item.id,
            'name': item_name,
            "message": f"{item_name} : symbole mise à jour",
        })
    elif action == "modify_name":
        old_name = item_name
        item_name = request.POST.get(
            "new_name_isovitesse_input",
        )
        item.name = item_name
        item.save()
        if item.etat:
            etat_id = item.etat.id
        return JsonResponse({
            'success': True,
            'id': item.id,
            'new_name': item_name,
            'old_name': old_name,
        })
    elif action == "active_all_item":
        lst_cas = Cas.objects.filter(iso_vitesse=item)
        ids = list(lst_cas.values_list("id", flat=True))
        lst_cas.update(used=True)
        lst_cas.update(calculate_perfo=False)
        total = len(ids)

        return JsonResponse({
            "success": True,
            "cas_ids": ids,
            "used_cas": total,
            "total_cas": total,
            "iso_vitesse_id": item.id,
            "name": item_name,
        })

    elif action == "desactive_all_item":
        lst_cas = Cas.objects.filter(iso_vitesse=item)
        ids = list(lst_cas.values_list("id", flat=True))
        lst_cas.update(used=False)
        lst_cas.update(calculate_perfo=False)

        total = len(ids)

        return JsonResponse({
            "success": True,
            "cas_ids": ids,
            "used_cas": 0,
            "total_cas": total,
            "iso_vitesse_id": item.id,
            "name": item_name,
        })

    elif action == "delete_iso_vitesse":
        isovitesse_name = item_name
        etat_id = item.etat.id
        Cas.objects.filter(iso_vitesse=item).delete()
        IsoVitesse.objects.get(pk=item.id).delete()
        messages.info(request, f"{isovitesse_name} : Isovitesse supprimé")
        return redirect("info_etat", etat_id=etat_id)

    # Renvoyer un JSON avec les informations nécessaires
    return JsonResponse(
        {
            "success": True,
        }
    )


@require_http_methods(["POST"])
def scan_repertoire(request, obj_type, etat_id):

    user_id = request.user.username

    etat = get_object_or_404(Etat, id=etat_id)

    temp_repertory = normalize_path_os(
        clean_user_ihm_path(request.POST.get("repertoire_cas_cannelle", ""))
    )
    temp_path = Path(temp_repertory)

    ok = (
        temp_path.exists()
        and temp_path.is_dir()
        and os.access(temp_path, os.R_OK)
        and user_permission(user_id, temp_path)
    )

    if ok:
        if obj_type == "cas_cannelle":
            etat.cas_temp_repertory = temp_repertory
        elif obj_type == "bsam":
            etat.bsam_temp_repertory = temp_repertory

        etat.save()
        messages.info(request, "Répertoire accessible par le serveur.")
    else:
        messages.error(request, "Répertoire non accessible")

    tab = request.GET.get("tab")
    url = reverse("info_etat", kwargs={"etat_id": etat.id})
    if tab:
        url = f"{url}?tab={tab}"

    return redirect(url)


def search_cas_cannelle(request, obj_type, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)

    # Récupère la requête de recherche (mot-clé)
    query = request.GET.get("q", "")

    if obj_type == 'cas_cannelle':
        all_cas_cannelle = os.listdir(etat.cas_temp_repertory)
        keywords = query.lower().split(
            "*")  # Séparer les mots-clés par l'astérisque
        filtered_cas_cannelle = [
            item
            for item in all_cas_cannelle
            if all(keyword in item.lower() for keyword in keywords)
        ]
        return JsonResponse({"results": filtered_cas_cannelle})
    elif obj_type == 'bsam':
        all_bsam_cannelle = os.listdir(etat.bsam_temp_repertory)
        keywords = query.lower().split(
            "*")  # Séparer les mots-clés par l'astérisque
        filtered_bsam = [
            item
            for item in all_bsam_cannelle
            if all(keyword in item.lower() for keyword in keywords)
        ]
        return JsonResponse({"results": filtered_bsam})


@require_http_methods(["POST"])
def update_recalage_kd(request, pk):
    try:
        data = json.loads(request.body)
        mode = data.get("mode")
        value = data.get("value")

        iso = IsoVitesse.objects.get(pk=pk)

        if mode == "oui":
            iso.recalage_kd_mode = "oui"
            iso.recalage_kd = str(float(value))

        elif mode == "non":
            iso.recalage_kd_mode = "non"
            iso.recalage_kd = "1"

        elif mode == "auto":
            iso.recalage_kd_mode = "auto"
            iso.recalage_kd = "AUTO"

        else:
            return JsonResponse(
                {"success": False, "error": "Mode invalide"},
                status=400
            )

        iso.save()
        return JsonResponse({"success": True})

    except IsoVitesse.DoesNotExist:
        return JsonResponse(
            {"success": False, "error": "IsoVitesse introuvable"},
            status=404
        )

    except ValueError:
        return JsonResponse(
            {"success": False, "error": "Valeur numérique invalide"},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e)},
            status=400
        )


def download_example_curve(request):
    file_path = (
        Path(settings.BASE_DIR)
        / "apps"
        / "templates"
        / "static_files"
        / "Exemple-user-curve.xls"
    )
    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename="Exemple-user-curve.xls"
    )


@require_http_methods(["POST"])
def update_graph_config(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)

    data = json.loads(request.body)
    conf = data.get("graph_configuration")

    cleaned = []
    for item in conf:
        if not isinstance(item, dict):
            continue

        x = item.get("x_axis")
        y = item.get("y_axis")

        if not isinstance(x, str) or not isinstance(y, str):
            continue

        cleaned.append({
            "x_axis": x.strip(),
            "y_axis": y.strip()
        })

    etat.graph_configuration = cleaned
    etat.save()

    return JsonResponse({"success": True})


@require_http_methods(["POST"])
def update_plan_selection(request, etat_id):

    etat = get_object_or_404(Etat, id=etat_id)
    data = json.loads(request.body or "{}")
    get_plane_configuration(etat)

    etat.refresh_from_db()

    plan_amont = (data.get("plan_amont") or "").strip()
    plan_aval = (data.get("plan_aval") or "").strip()

    # Listes dispo (stockées sur l'état)
    available_amont = etat.plan_amont or ["Inlet"]
    available_aval = etat.plan_aval or ["Outlet"]

    # Sécurisation : si la valeur choisie n'est pas dans la liste, fallback
    if plan_amont not in available_amont:
        plan_amont = "Inlet"

    if plan_aval not in available_aval:
        plan_aval = "Outlet"

    etat.plan_amont_selected = plan_amont
    etat.plan_aval_selected = plan_aval
    etat.save(update_fields=["plan_amont_selected", "plan_aval_selected"])

    iso_vitesses_hdf = IsoVitesse.objects.filter(etat=etat, file_type="hdf")
    Cas.objects.filter(iso_vitesse__in=iso_vitesses_hdf).update(
        calculate_perfo=False)

    return JsonResponse({
        "success": True,

        # sélection confirmée
        "plan_amont_selected": plan_amont,
        "plan_aval_selected": plan_aval,

        # listes disponibles
        "plan_amont": available_amont,
        "plan_aval": available_aval,
    })




