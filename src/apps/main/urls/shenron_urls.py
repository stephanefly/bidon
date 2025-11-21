
from django.urls import path
from apps.main.views import (lst_projets_shenron, delete_projet_shenron,
                             rename_projet_shenron, info_projet_shenron)

urlpatterns = [
    path('shenron/', lst_projets_shenron, name='lst_projets_shenron'),
    path('shenron/<int:projet_shenron_id>/', info_projet_shenron, name="info_projet_shenron"),
    path('shenron/delete/<int:projet_shenron_id>/', delete_projet_shenron, name='delete_projet_shenron'),
    path('shenron/rename/<int:projet_shenron_id>/', rename_projet_shenron, name='rename_projet_shenron'),
]
