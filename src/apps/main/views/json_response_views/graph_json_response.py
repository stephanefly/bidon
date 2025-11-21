import json
from os.path import basename
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from apps.main.models import Cas, Etat


@csrf_exempt
def save_selection(request, etat_id):
    etat = Etat.objects.get(id=etat_id)
    if request.method == "POST":
        body = json.loads(request.body)
        selected_cases_id = body.get("selected_cases_id", [])
        selected_cases = body.get("selected_cases", [])

        print(selected_cases_id, selected_cases)

        if selected_cases_id:

            with transaction.atomic():
                # Étape 1. Tout désélectionner
                Cas.objects.filter(iso_vitesse__etat=etat).update(
                    select=False)

                # Étape 2 : Séparer les éléments .bsam
                cas_ids = []

                # Requêtes groupées
                cas_queryset = Cas.objects.filter(
                    pk__in=selected_cases_id).values('id', 'name')


                # Dictionnaires d'accès rapide
                cas_dict = {obj['id']: obj['name'] for obj in cas_queryset}


                # Séparation des cas vs bsam selon le nom
                for case_name, case_id in zip(selected_cases,
                                              selected_cases_id):
                    if case_id in cas_dict and case_name == cas_dict[case_id]:
                        cas_ids.append(case_id)


                # Étape 3 : Réactiver les éléments sélectionnés
                Cas.objects.filter(id__in=cas_ids,
                                   iso_vitesse__etat=etat).update(select=True)

            message = "Sélection mise à jour avec succès."
        else:
            # Si aucune sélection n'est faite, déselectionner tous les cas
            Cas.objects.filter(iso_vitesse__etat=etat).update(select=False)

        return JsonResponse({})
