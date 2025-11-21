from django.contrib import admin
from .models import UtilitaireConfiguration


@admin.register(UtilitaireConfiguration)
class UtilitaireConfigurationAdmin(admin.ModelAdmin):
    list_display = ("user", "genepi_path", "cannelle_path")
    readonly_fields = ("user",)
    list_filter = ("user",)
# Register your models here.
