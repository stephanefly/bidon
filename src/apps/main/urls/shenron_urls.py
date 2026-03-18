from django.urls import path
from apps.main import views

urlpatterns = [
    path("lst_projets_shenron/", views.lst_projets_shenron, name="lst_projets_shenron"),
    path("lst_projets_shenron/<int:projet_shenron_id>/generer_shenron_script/",views.generer_shenron_script,name="generer_shenron_script"),
    path("lst_projets_shenron/<int:projet_shenron_id>/", views.info_projet_shenron, name="info_projet_shenron"),
    path("lst_projets_shenron/<int:projet_shenron_id>/save/", views.save_projet_shenron, name="save_projet_shenron"),
    path("lst_projets_shenron/<int:projet_sheron_id>/delete/", views.delete_projet_shenron, name="delete_projet_shenron"),
    path("lst_projets_shenron/<int:projet_sheron_id>/rename/", views.rename_projet_shenron, name="rename_projet_shenron"),
]