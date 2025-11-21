# apps/main/urls/base_urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from apps.main.views import (
    accueil,
    configuration_view,
    defreeze_etat,
    delete_etat,
    delete_projet,
    duplicate_etat,
    freeze_etat,
    info_etat,
    info_projet,
    lst_projets,
    rename_etat,
    rename_projet,
    recherche_globale,
    explorer,
    split_pdf,
)

urlpatterns = [
    # main/urls.py
    path("", accueil, name="accueil"),
    path(
        "login/",
        LoginView.as_view(template_name="django_login/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),  # ou '/trunks/' si c'est ta home
        name="logout",
    ),

    path("lst_projets", lst_projets, name="lst_projets"),

    # Projets
    path("projects/delete/<int:projet_id>/", delete_projet, name="delete_projet"),
    path("projects/rename/<int:projet_id>/", rename_projet, name="rename_projet"),
    path("lst_projets/<int:projet_id>/", info_projet, name="info_projet"),

    # États
    path("lst_projets/etat/duplicate/<int:etat_id>/", duplicate_etat, name="duplicate_etat"),
    path("lst_projets/etat/delete/<int:etat_id>/", delete_etat, name="delete_etat"),
    path("lst_projets/etat/freeze/<int:etat_id>/", freeze_etat, name="freeze_etat"),
    path("lst_projets/etat/defreeze/<int:etat_id>/", defreeze_etat, name="defreeze_etat"),
    path("lst_projets/etat/rename/<int:etat_id>/", rename_etat, name="rename_etat"),
    path("lst_projets/etat/<int:etat_id>/", info_etat, name="info_etat"),

    # Configuration
    path("configuration", configuration_view, name="configuration"),
    path('recherche/', recherche_globale, name='recherche_globale'),

    # Explorer
    path("explorer", explorer, name="explorer"),

    # Split PDF
    path("tools/split-pdf/", split_pdf, name="split_pdf"),
]
