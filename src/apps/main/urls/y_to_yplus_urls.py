from django.urls import path

from apps.main.views import utilitaire_y_to_yplus

urlpatterns = [
    path("utilitaire_y_to_yplus", utilitaire_y_to_yplus, name="utilitaire_y_to_yplus"),
]
