from django.urls import path

from apps.main.views import (lst_revue_aube, info_revue_aube,
                             delete_revue_aube, rename_revue_aube, aube_create,
                             aube_update, aube_delete, aube_duplicate,
                             launch_revue_aube, active_aube, afficher_code_dico,
                             telecharger_code_dico, changer_dico)


urlpatterns = [
    path("lst_revue_aube", lst_revue_aube, name="lst_revue_aube"),
    path("lst_revue_aube/<int:revue_aube_id>/", info_revue_aube, name="info_revue_aube"),
    path("delete_revue_aube/<int:revue_aube_id>/", delete_revue_aube, name="delete_revue_aube"),
    path("rename_revue_aube/<int:revue_aube_id>/", rename_revue_aube,name="rename_revue_aube"),
    # path("remove_bsam/<int:revue_veine_id>/<int:cas_id>/", remove_bsam, name="remove_bsam"),
    path("revues-aube/<int:revue_aube_id>/aubes/ajouter/", aube_create,name="aube_create"),
    path("lst_revue_aube/<int:revue_aube_id>/aubes/<int:aube_id>/modifier/",aube_update, name="aube_update"),
    path("lst_revue_aube/<int:revue_aube_id>/aubes/<int:aube_id>/supprimer/",aube_delete, name="aube_delete"),
    path("lst_revue_aube/<int:revue_aube_id>/aube/<int:aube_id>/duplicate/", aube_duplicate, name="aube_duplicate"),
    path("launch_revue_aube/<int:revue_aube_id>/",launch_revue_aube, name="launch_revue_aube"),
    path("lst_revue_aube/<int:revue_aube_id>/active_aube/<int:aube_id>/", active_aube, name="active_aube"),
    path('afficher_code_dico/<int:pk>/', afficher_code_dico,name='afficher_code_dico'),
    path('telecharger_dico/<int:pk>/', telecharger_code_dico,name='telecharger_code_dico'),
    path('changer_dico/<int:pk>/', changer_dico, name='changer_dico'),

]
