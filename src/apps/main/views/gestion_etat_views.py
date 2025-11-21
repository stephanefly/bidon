import os
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.urls import reverse
import os, uuid, pathlib
import pandas as pd
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from apps.main.models import Cas, Etat, IsoVitesse, Row, RowPair, Aube
from apps.main.modules.gestion_projets.tools import get_color_list, get_symbol_list
from apps.main.modules.graph_perfo_0d.user_case import (lecture_user_file_curve,
                                                        dico_listes_par_colonne, build_config_row, build_row_list, save_to_database)

# Vue pour afficher l'état et les Cas associés
def info_etat(request, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    projet = etat.projet
    # Récupère tous les noms existants pour l'état donné
    lst_iso_vitesse = IsoVitesse.objects.filter(etat=etat).order_by('file_type')
    lst_cas = Cas.objects.filter(iso_vitesse__in=lst_iso_vitesse)
    all_case_used = sum(iso.used_cas() for iso in lst_iso_vitesse)

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
                new_cas = Cas.objects.create(
                    name=cas_name,
                    iso_vitesse=iso_vitesse,
                    obj_type="cas_cannelle"
                )
                new_cas.set_repertory_path()

                new_cas.get_bsam_file()

                if file_type == "hdf":
                    new_cas.get_hdf5_path()
                else:
                    new_cas.get_excel_path()
                new_cas.save()

        return redirect("info_etat", etat_id=etat.id)

    if request.method == "POST" and request.POST.getlist("selected_multiple_item2"):
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
            if bsam_name not in Cas.objects.filter(
                    iso_vitesse__in=lst_iso_vitesse,obj_type="bsam"
            ):

                new_bsam = Cas.objects.create(
                    name=bsam_name,
                    iso_vitesse=iso_vitesse,
                    obj_type="bsam"
                )

                new_bsam.set_repertory_path()
                new_bsam.get_bsam_file()
                new_bsam.save()

        return redirect(f"{reverse('info_etat', args=[etat.id])}?tab=2")

    if request.method == "POST" and request.POST.getlist("name_isovitesse_input3"):
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
    if model_name == "cas":
        model = Cas
    if model_name == "iso_vitesse":
        model = IsoVitesse
    if model_name == "aube":
        model = Aube

    item = get_object_or_404(model, id=item_id)

    if action == "active":
        item.used = not item.used  # Inverse la valeur de used
        item.save()
        if item.iso_vitesse.etat:
            etat_id = item.iso_vitesse.etat.id
        # Calcul des valeurs mises à jour pour IsoVitesse
        iso_vitesse = item.iso_vitesse
        used_cas = iso_vitesse.used_cas()
        total_cas = iso_vitesse.total_cas()

        # Renvoyer un JSON avec les informations nécessaires
        return JsonResponse(
            {
                "success": True,
                "used": item.used,
                "iso_vitesse_id": iso_vitesse.id,
                "used_cas": used_cas,
                "total_cas": total_cas,
            }
        )
    elif action == "delete":
        etat_id = item.iso_vitesse.etat.id
        if len(Cas.objects.filter(iso_vitesse=item.iso_vitesse)) == 1:
            item.delete()
            item.iso_vitesse.delete()
        else:
            item.delete()
    elif action == "update_color":
        new_color = (
                request.POST.get("color_aube")
                or request.POST.get("color_isovitesse")
                or "black"
        )
        item.color = new_color
        item.save()
    elif action == "update_symbol":
        new_marker = request.POST.get(
            "symbole_isovitesse",
        )  # Défaut à noir si aucune couleur n'est sélectionnée
        item.marker = new_marker
        item.save()
        if item.etat:
            etat_id = item.etat.id
    elif action == "modify_name":
        item.name = request.POST.get(
            "new_name_isovitesse_input",
        )
        item.save()
        if item.etat:
            etat_id = item.etat.id
        return JsonResponse({
            'success': True,
            'id': item.id,
            'new_name': item.name
        })
    elif action == "active_all_item":
        lst_cas = Cas.objects.filter(iso_vitesse=item)
        ids = []
        for cas in lst_cas:
            cas.used = True
            cas.save()
            ids.append(cas.id)
        # Renvoyer un JSON avec les informations nécessaires
        return JsonResponse({
            "success": True,
            "cas_ids": ids,
            "used_cas": len(ids),
            "total_cas": len(ids),
            "iso_vitesse_id": item.id
        })
    elif action == "desactive_all_item":
        lst_cas = Cas.objects.filter(iso_vitesse=item)
        ids = []
        for cas in lst_cas:
            cas.used = False
            cas.save()
            ids.append(cas.id)

        etat_id = item.etat.id
        # Renvoyer un JSON avec les informations nécessaires
        return JsonResponse({
            "success": True,
            "cas_ids": ids,
            "used_cas": 0,
            "total_cas": len(ids),
            "iso_vitesse_id": item.id
        })
    elif action == "delete_iso_vitesse":
        etat_id = item.etat.id
        Cas.objects.filter(iso_vitesse=item).delete()
        IsoVitesse.objects.get(pk=item.id).delete()
        return redirect("info_etat", etat_id=etat_id)

    return JsonResponse({"status": "ok"}, status=200)


@require_http_methods(["POST"])
def scan_repertoire(request, obj_type, etat_id):
    etat = get_object_or_404(Etat, id=etat_id)
    temp_repertory = request.POST.get("repertoire_cas_cannelle", "").strip()

    if obj_type == 'cas_cannelle':
        etat.cas_temp_repertory = temp_repertory
    elif obj_type == 'bsam':
        etat.bsam_temp_repertory = temp_repertory

    etat.save()

    # On récupère le tab envoyé dans l'URL du formulaire (ex: ?tab=2)
    tab = request.GET.get("tab")

    # On construit l'URL de base
    url = reverse("info_etat", kwargs={"etat_id": etat.id})

    # Si un onglet est précisé, on le remet dans la redirection
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
        value = data.get('value', None)

        iso = IsoVitesse.objects.get(pk=pk)
        if value in ("", None):
            iso.recalage_kd = None
        else:
            iso.recalage_kd = float(value)
        iso.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
