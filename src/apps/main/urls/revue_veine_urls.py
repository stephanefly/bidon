from django.urls import path

from apps.main.views import (
    ajouter_bsam,
    create_new_revue_veine,
    delete_revue_veine,
    download_pdf_trace_veine,
    export_graph_detais_bsam,
    info_revue_veine,
    lst_revue_veine,
    remove_bsam,
    rename_revue_veine,
    add_revue_veine,
    duplicate_revue_veine,
)

urlpatterns = [
    path("lst_revue_veine", lst_revue_veine, name="lst_revue_veine"),
    path("add_revue_veine", add_revue_veine, name="add_revue_veine"),
    path("create_new_revue_veine", create_new_revue_veine, name="create_new_revue_veine"),
    path("lst_revue_veine/<int:revue_veine_id>/", info_revue_veine, name="info_revue_veine"),
    path("delete_revue_veine/<int:revue_veine_id>/", delete_revue_veine, name="delete_revue_veine"),
    path("remove_bsam/<int:revue_veine_id>/<int:cas_id>/", remove_bsam, name="remove_bsam"),
    path("rename_revue_veine/<int:revue_veine_id>/", rename_revue_veine, name="rename_revue_veine"),
    path('revue_veine/<int:revue_veine_id>/ajouter_bsam/', ajouter_bsam, name='ajouter_bsam'),
    path("download_pdf_trace_veine/<int:revue_veine_id>/", download_pdf_trace_veine, name="download_pdf_trace_veine"),
    path("export_html_graph_detais_bsam/<int:revue_veine_id>/", export_graph_detais_bsam, name="export_graph_detais_bsam"),
    path("lst_revue_veine/duplicate/<int:revue_veine_id>/", duplicate_revue_veine,name="duplicate_revue_veine"),
]
