from django.urls import path

from apps.main.views import (
    delete_revue_veine,
    download_pdf_trace_veine,
    export_graph_detais_bsam,
    get_image,
    info_revue_veine,
    lst_revue_veine,
    rename_revue_veine,
    remove_bsam,
ajouter_bsam, create_new_revue_veine
)

urlpatterns = [
    path("lst_revue_veine", lst_revue_veine, name="lst_revue_veine"),
    path("create_new_revue_veine", create_new_revue_veine, name="create_new_revue_veine"),
    path("lst_revue_veine/<int:revue_veine_id>/", info_revue_veine, name="info_revue_veine"),
    path("delete_revue_veine/<int:revue_veine_id>/", delete_revue_veine, name="delete_revue_veine"),
    path("remove_bsam/<int:revue_veine_id>/<int:cas_id>/", remove_bsam, name="remove_bsam"),
    path("rename_revue_veine/<int:revue_veine_id>/", rename_revue_veine, name="rename_revue_veine"),
    path("media/trace_veine/<int:revue_veine_id>/", get_image, name="get_image"),
    path('revue_veine/<int:revue_veine_id>/ajouter_bsam/', ajouter_bsam, name='ajouter_bsam'),
    path("download_pdf_trace_veine/<int:revue_veine_id>/", download_pdf_trace_veine, name="download_pdf_trace_veine"),
    path("export_html_graph_detais_bsam/<int:revue_veine_id>/", export_graph_detais_bsam, name="export_graph_detais_bsam"),
]
