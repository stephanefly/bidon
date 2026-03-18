from django.contrib import admin
from django.db.models import Count

from .models import (
    UtilitaireConfiguration,
    RevueVeine,
    ProjetShenron,
    RevueAube,
    Aube,
    Project,
    Etat,
    IsoVitesse,
    Cas,
    Row,
    RowPair,
    Stat
)

# =========================
# INLINES (affichés dans d'autres pages)
# =========================

class IsoVitesseInline(admin.TabularInline):
    model = IsoVitesse
    extra = 0
    fields = ("name", "file_type", "color", "marker", "recalage_kd")
    show_change_link = True


class CasInline(admin.TabularInline):
    model = Cas
    extra = 0
    fields = ("name", "obj_type", "available", "used", "calculate_perfo", "select")
    show_change_link = True


class RowInline(admin.TabularInline):
    model = Row
    extra = 0
    fields = ("position", "name", "flux", "omega", "nb_blade", "bsam_name")
    show_change_link = True


class RowPairInline(admin.TabularInline):
    model = RowPair
    extra = 0
    fields = ("name", "type", "entry_row", "exit_row", "Qcorr_ref", "Pi", "Etapol")
    show_change_link = True


# =========================
# ADMINS
# =========================

@admin.register(UtilitaireConfiguration)
class UtilitaireConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "genepi_path",
        "cannelle_path",
        "anNA_path",
        "carma_path",
        "ensight_path",
        "genepi_auto_path",
        "user_directory",
    )
    readonly_fields = ("user",)
    list_filter = ("user",)
    search_fields = ("user__username", "user__email", "user_directory")


@admin.register(RevueVeine)
class RevueVeineAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "created_at", "work_directory", "nb_cas")
    list_filter = ("created_by", "created_at")
    search_fields = ("name", "created_by", "work_directory")
    ordering = ("-created_at",)
    inlines = (CasInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_nb_cas=Count("cas"))

    def nb_cas(self, obj):
        return getattr(obj, "_nb_cas", 0)
    nb_cas.admin_order_field = "_nb_cas"
    nb_cas.short_description = "Cas"


@admin.register(ProjetShenron)
class ProjetShenronAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "created_at", "work_directory")
    list_filter = ("created_by", "created_at")
    search_fields = ("name", "created_by", "work_directory")
    ordering = ("-created_at",)


@admin.register(RevueAube)
class RevueAubeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "created_at", "work_directory", "dico_genepi_auto", "nb_aubes")
    list_filter = ("created_by", "created_at")
    search_fields = ("name", "created_by", "work_directory", "dico_genepi_auto")
    ordering = ("-created_at",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_nb_aubes=Count("aube"))

    def nb_aubes(self, obj):
        return getattr(obj, "_nb_aubes", 0)
    nb_aubes.admin_order_field = "_nb_aubes"
    nb_aubes.short_description = "Aubes"


@admin.register(Aube)
class AubeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "projet",
        "version",
        "aube",
        "type_coupe_nbre_ldc",
        "label_bsam",
        "calage_deg",
        "inversion_aube",
        "inversion_bsam",
        "used",
        "revue_aube",
    )
    list_filter = (
        "used",
        "inversion_aube",
        "inversion_bsam",
        "revue_aube",
        "projet",
        "version",
    )
    search_fields = (
        "projet",
        "version",
        "aube",
        "type_coupe_nbre_ldc",
        "coupe_dessin",
        "label_bsam",
        "titre_cas",
        "fichier_bsam",
        "lien_xml",
    )
    ordering = ("-id",)
    list_per_page = 50
    autocomplete_fields = ("revue_aube",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "work_directory")
    list_filter = ("created_by",)
    search_fields = ("name", "created_by", "work_directory")
    ordering = ("name",)

    # Voir tous les états dans le projet
    # (si tu veux aussi inline Etat, dis-moi, sinon ça peut être lourd)


@admin.register(Etat)
class EtatAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "projet",
        "freeze",
        "created_by",
        "modify_by",
        "created_at",
        "updated_at",
        "work_directory",
        "cas_temp_repertory",
        "bsam_temp_repertory",
        "nb_iso",
    )
    list_filter = ("freeze", "projet", "created_by", "created_at", "updated_at")
    search_fields = ("name", "work_directory", "created_by", "modify_by")
    ordering = ("-updated_at",)
    list_per_page = 50
    inlines = (IsoVitesseInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("projet").annotate(_nb_iso=Count("isovitesse"))

    def nb_iso(self, obj):
        return getattr(obj, "_nb_iso", 0)
    nb_iso.admin_order_field = "_nb_iso"
    nb_iso.short_description = "IsoVitesse"


@admin.register(IsoVitesse)
class IsoVitesseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "etat",
        "file_type",
        "color",
        "marker",
        "recalage_kd",
        "total_cas",
        "used_cas",
    )
    list_filter = ("file_type", "etat")
    search_fields = ("name", "etat__name", "etat__projet__name")
    ordering = ("name",)
    list_per_page = 50
    autocomplete_fields = ("etat",)
    inlines = (CasInline,)

    # IMPORTANT: évite d'appeler total_cas/used_cas si tu as des milliers de cas,
    # mais c'est ultra pratique pour toi au quotidien.


@admin.register(Cas)
class CasAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "obj_type",
        "available",
        "used",
        "calculate_perfo",
        "select",
        "iso_vitesse",
        "etat",
        "revue_veine",
        "file_path",
        "bsam_path",
        "repertory",
    )

    list_filter = (
        "obj_type",
        "available",
        "used",
        "calculate_perfo",
        "select",
        "revue_veine",
        "iso_vitesse",
    )

    search_fields = (
        "name",
        "file_path",
        "bsam_path",
        "repertory",
        "iso_vitesse__name",
        "iso_vitesse__etat__name",
        "revue_veine__name",
    )

    ordering = ("name",)
    list_editable = ("available", "used", "select")
    list_per_page = 50
    autocomplete_fields = ("iso_vitesse", "revue_veine")
    inlines = (RowInline, RowPairInline)

    fieldsets = (
        ("Identification", {"fields": ("name", "obj_type", "revue_veine", "iso_vitesse")}),
        ("Statut", {"fields": ("available", "used", "select", "calculate_perfo")}),
        ("Fichiers", {"fields": ("file_path", "bsam_path", "repertory")}),
        ("Métadonnées", {"classes": ("collapse",), "fields": ("row_metadata",)}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("iso_vitesse", "iso_vitesse__etat", "revue_veine")

    def etat(self, obj):
        if obj.iso_vitesse and obj.iso_vitesse.etat:
            return obj.iso_vitesse.etat
        return None
    etat.short_description = "Etat"


@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cas",
        "position",
        "name",
        "flux",
        "omega",
        "nb_blade",
        "bsam_name",
    )
    list_filter = ("cas",)
    search_fields = ("name", "flux", "bsam_name", "cas__name")
    ordering = ("cas", "position")
    list_per_page = 100
    autocomplete_fields = ("cas",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("cas")


@admin.register(RowPair)
class RowPairAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cas",
        "name",
        "type",
        "entry_row",
        "exit_row",
        "Qcorr_ref",
        "Pi",
        "Etapol",
        "Qcorr",
        "Cd",
        "Tau",
        "PisQcorr_ref",
    )
    list_filter = ("cas", "type")
    search_fields = ("name", "cas__name")
    ordering = ("cas", "name")
    list_per_page = 100
    autocomplete_fields = ("cas", "entry_row", "exit_row")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("cas", "entry_row", "exit_row")

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "created_at",
    )

    list_filter = (
        "name",
        "user",
        "created_at",
    )

    search_fields = (
        "name",
        "user",
    )

    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    readonly_fields = ("created_at",)

    list_per_page = 50