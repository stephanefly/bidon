from django.urls import path

from apps.main.views import (
    launch_genepi_auto_from_perfo,
    change_item,
    affichage_modal_create_revue_veine_from_perfo0D,
    graph_perfo_0d,
    scan_repertoire,
    search_cas_cannelle,
    trace_conv,
    update_recalage_kd, download_example_curve, update_graph_config,
    update_plan_selection
)
from apps.main.views.json_response_views.graph_json_response import (
    save_selection,
)

urlpatterns = [
    # Graphiques Perfo 0D
    path("lst_projets/etat/graph_perfo_0d/<int:etat_id>/", graph_perfo_0d, name="graph_perfo_0d"),
    # path("save_graph_changes/<int:graph_state_id>/", save_graph_changes, name="save_graph_changes"),
    path("save_selection/<int:etat_id>/", save_selection,name="save_selection"),
    path('update_recalage_kd/<int:pk>/', update_recalage_kd, name='update_recalage_kd'),
    path("etat/<int:etat_id>/update_graph_config/", update_graph_config,
         name="update_graph_config"),
    path("etat/<int:etat_id>/update_plan_selection/", update_plan_selection,
         name="update_plan_selection"),

    # Scans et cas spécifiques
    path("scan_repertoire/<str:obj_type>/<int:etat_id>/", scan_repertoire, name="scan_repertoire"),
    path("search_cas_cannelle/<str:obj_type>/<int:etat_id>/", search_cas_cannelle, name="search_cas_cannelle"),
    path("download/example-curve/", download_example_curve, name="download_example_curve"),

    # Actions génériques sur les items
    path("<str:model_name>/<int:item_id>/active/", change_item, {"action": "active"}, name="active_item"),
    path("<str:model_name>/<int:item_id>/delete/", change_item, {"action": "delete"}, name="delete_item"),
    path("<str:model_name>/<int:item_id>/update_color/", change_item, {"action": "update_color"}, name="update_color_item"),
    path("<str:model_name>/<int:item_id>/update_symbol/", change_item,{"action": "update_symbol"}, name="update_symbol_item"),
    path("<str:model_name>/<int:item_id>/open_folder/", change_item, {"action": "open_folder"}, name="open_folder_item"),
    path("<str:model_name>/<int:item_id>/modify_name/", change_item, {"action": "modify_name"}, name="modify_name_item"),
    path("<str:model_name>/<int:item_id>/active_all_item/", change_item, {"action": "active_all_item"}, name="active_all_item"),
    path("<str:model_name>/<int:item_id>/desactive_all_item/", change_item, {"action": "desactive_all_item"}, name="desactive_all_item"),
    path("<str:model_name>/<int:item_id>/delete_iso_vitesse/", change_item,{"action": "delete_iso_vitesse"}, name="delete_iso_vitesse"),

    # Action spécifique
    path("launch_genepi_auto_from_perfo/<int:etat_id>/", launch_genepi_auto_from_perfo, name="launch_genepi_auto_from_perfo"),
    path("trace_conv/<int:etat_id>/", trace_conv, name="trace_conv"),
    path("create_revue_veine/<int:etat_id>/", affichage_modal_create_revue_veine_from_perfo0D, name="affichage_modal_create_revue_veine_from_perfo0D"),

]
