import os
from pathlib import Path
from apps.main.modules.gestion_projets.tools import get_user_path
from datetime import datetime

from django.utils.timezone import now
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class UtilitaireConfiguration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genepi_path = models.CharField(max_length=255, blank=True, null=True)
    cannelle_path = models.CharField(max_length=255, blank=True, null=True)
    anNA_path = models.CharField(max_length=255, blank=True, null=True)
    carma_path = models.CharField(max_length=255, blank=True, null=True)
    ensight_path = models.CharField(max_length=255, blank=True, null=True)
    genepi_auto_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'main'

class RevueVeine(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    directory = models.CharField(max_length=255, blank=True, null=True)


    def get_image_path(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"TraceVeine_{self.name}_{timestamp}.jpg"  # Extension à adapter si besoin
        return os.path.join(self.directory, filename)


class ProjetShenron(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    work_dir= models.CharField(max_length=255, blank=True)

class RevueAube(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    work_dir= models.CharField(max_length=255, blank=True)
    dico_genepi_auto = models.CharField(
        max_length=255,
        default="apps/main/modules/genepi/GENEPIAuto_Dico - TRUNKS - Defaut .py"
    )
    # TODO: grille

class Aube(models.Model):

    color = models.CharField(max_length=255, null=False, blank=True, default="black")
    projet = models.CharField(max_length=100, blank=True, default="CME3")
    version = models.CharField(max_length=100, blank=True, default="S1")
    aube = models.CharField(max_length=100, blank=True, default="S1AB")
    type_coupe_nbre_ldc = models.CharField(max_length=50, blank=True, default="CQ")
    coupe_dessin = models.CharField(max_length=200, blank=True, default="1,11,15,19,29")
    label_bsam = models.CharField(max_length=50, blank=True, default="S1")
    inversion_aube = models.BooleanField(default=False)
    fichier_bsam = models.CharField(max_length=255, blank=True)
    inversion_bsam = models.BooleanField(default=False)
    calage_deg = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    titre_cas = models.CharField(max_length=100, blank=True)
    lien_xml = models.CharField(max_length=255, blank=True)
    revue_aube = models.ForeignKey(
        RevueAube, on_delete=models.SET_NULL, null=True, blank=True
    )
    used = models.BooleanField(default=True)

    def __str__(self):
        return f"Aube {self.id} - {self.projet_version_aube}"
    def save(self, *args, **kwargs):
        if self.fichier_bsam:
            self.fichier_bsam = self.fichier_bsam.replace('"', '').strip()
        if self.lien_xml:
            self.lien_xml = self.lien_xml.replace('"', '').strip()
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=255)
    work_directory = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def rename_project(self, new_name):
        new_path = os.path.join(get_user_path(self), new_name)
        os.rename(self.work_directory, new_path)
        self.name = new_name
        self.work_directory = new_path
        self.save()


class Etat(models.Model):
    name = models.CharField(max_length=100)
    projet = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, blank=True
    )
    freeze = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255)
    modify_by = models.CharField(max_length=255, default="")
    work_directory = models.CharField(max_length=255)
    cas_temp_repertory = models.CharField(max_length=255, blank=True, null=True)
    bsam_temp_repertory = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def maj_work_directory(self):
        new_path = os.path.join(self.projet.work_directory, self.name)
        self.work_directory = new_path
        self.save()

    def rename_etat(self, new_name):
        new_path = os.path.join(self.projet.work_directory, new_name)
        os.rename(self.work_directory, new_path)
        self.name = new_name
        self.work_directory = new_path
        self.save()

    def get_cache_filepath(self):
        timestamp = self.updated_at.strftime("%Y%m%d%H%M%S")
        filename = f"cache-data-etat{timestamp}.json"
        if not os.path.exists(os.path.join(self.work_directory, "data-cache")):
            os.makedirs(os.path.join(self.work_directory, "data-cache"))
        return os.path.join(self.work_directory, "data-cache" ,filename)

    def clean_old_cache_files(self):
        current_filename = self.get_cache_filepath()
        cache_filepath = os.path.join(self.work_directory, "data-cache")
        if os.path.exists(cache_filepath):
            for f in os.listdir(cache_filepath):
                if f.startswith("cache-data-etat") and f.endswith(".json"):
                    full_path = os.path.join(self.work_directory, "data-cache", f)
                    if full_path != current_filename:
                        os.remove(full_path)


class IsoVitesse(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=255, default="black")
    etat = models.ForeignKey(Etat, on_delete=CASCADE, null=True, blank=True)
    FILE_TYPE = [
        ("excel", "Excel (.xls)"),
        ("hdf", "hdf (.trac)"),
        ("bsam", "Bsam (.bsam)"),
    ]
    file_type = models.CharField(max_length=20, choices=FILE_TYPE, default="Excel")
    MARKERS = [
        ("circle", "Cercle ●"),
        ("square", "Carré ■"),
        ("triangle", "Triangle Haut ▲"),
        ("inverted_triangle", "Triangle Bas ▼"),
        ("x", "Croix ✕"),
        ("cross", "Plus ✚"),
        ("asterisk", "Étoile ✱"),
        ("hex", "Hexagone ⬡"),
    ]
    marker = models.CharField(max_length=255, choices=MARKERS, default="circle")
    row_config = models.JSONField(default=dict)
    recalage_kd = models.FloatField(null=True, blank=True, default=1)

    def __str__(self):
        return self.name

    def total_cas(self):
        return self.cas_set.count()

    def used_cas(self):
        return self.cas_set.filter(used=True).count()

    def get_lst_row_config(self):
        ordre = ['global', 'etage', 'pseudo_etage', 'isole']
        lst_row_config = []
        for key in ordre:
            lst_row_config.extend(self.row_config.get(key, []))
        return lst_row_config

    def get_indexed_dict(self):
        return {name: idx + 1 for idx, name in enumerate(
            self.get_lst_row_config())}

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.etat:
            self.etat.updated_at = now()
            self.etat.save(update_fields=["updated_at"])
            self.cas_set.exclude(obj_type='cas_utilisateur').update(
                calculate_perfo=False)

    def get_type_of_row_with_config(self, pair_row):
        ordre = ['global', 'etage', 'pseudo_etage', 'isole']
        for cle in ordre:
            if pair_row in self.row_config.get(cle, []):
                return cle


class Cas(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    used = models.BooleanField(default=True)
    calculate_perfo = models.BooleanField(default=False)
    iso_vitesse = models.ForeignKey(
        IsoVitesse,
        on_delete=CASCADE,null=True, blank=True)
    file_path = models.CharField(max_length=255)
    select = models.BooleanField(default=False)
    bsam_path = models.CharField(max_length=255, null=True, blank=True)
    repertory = models.CharField(max_length=255, blank=True, null=True)
    OBJ_TYPE_CHOICES = [
        ("cas_cannelle", "Cas Cannelle"),
        ("bsam", "Cas Bsam"),
        ("cas_utilisateur", "Cas Utilisateur"),
    ]
    obj_type = models.CharField(max_length=20, choices=OBJ_TYPE_CHOICES, default="cas_cannelle")
    row_metadata = models.JSONField(default=dict, blank=True)
    revue_veine = models.ForeignKey(RevueVeine, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.obj_type})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.iso_vitesse.etat:
            self.iso_vitesse.etat.updated_at = now()
            self.iso_vitesse.etat.save(update_fields=["updated_at"])

    def set_repertory_path(self):
        if self.obj_type == "cas_cannelle" and self.iso_vitesse:
            self.repertory = os.path.join(
                self.iso_vitesse.etat.cas_temp_repertory,
                self.name
            )
        elif self.obj_type == "bsam" and self.iso_vitesse:
            self.repertory = self.iso_vitesse.etat.bsam_temp_repertory

    def get_hdf5_path(self):
        hdf5_path = os.path.join(
            self.repertory,
            settings.HDF5_PATH,
        )

        if os.path.exists(hdf5_path):
            self.file_path = hdf5_path
            self.available = True
        self.save()

    def get_excel_path(self):
        # Liste des fichiers possibles dans l'ordre de priorité
        candidates = [
            settings.EXCEL_POST_ANNA_PATH_10,
            settings.EXCEL_POST_ANNA_PATH_7,
            settings.EXCEL_POST_ANTARES_PATH_10,
            settings.EXCEL_POST_ANTARES_PATH_7,
        ]

        # Recherche du premier fichier existant
        self.available = False
        for filename in candidates:
            path = os.path.join(self.repertory, filename)
            if os.path.exists(path):
                self.file_path = path
                self.available = True
                break

        self.save()

    def get_bsam_file(self):
        if self.obj_type == "cas_cannelle":
            bsam_path = os.path.join(
                self.repertory,
                settings.BSAM_PATH,
            )
            self.bsam_path = bsam_path
        else:
            self.bsam_path = os.path.join(
                self.repertory,
                self.name,
            )
            self.file_path = os.path.join(
                self.repertory,
                self.name,
            )
        self.save()
        return self.bsam_path


class Row(models.Model):
    cas = models.ForeignKey(Cas, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    flux = models.CharField(max_length=100, null=True, blank=True)
    position = models.IntegerField()
    omega = models.FloatField(null=True, blank=True)
    nb_blade = models.IntegerField(null=True, blank=True)
    bsam_name = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=10, editable=False)

    def set_row_type(self):
        row_type = 'rotor' if self.omega != 0.0 else 'stator'
        return row_type


class RowPair(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    cas = models.ForeignKey(Cas, on_delete=models.CASCADE, null=True, blank=True)
    entry_row = models.ForeignKey(Row, on_delete=models.CASCADE, null=True, blank=True, related_name='as_entry_row')
    exit_row = models.ForeignKey(Row, on_delete=models.CASCADE, null=True, blank=True, related_name='as_exit_row')
    name = models.CharField(max_length=100, blank=True)
    Qcorr_ref = models.FloatField(null=True)
    Pi = models.FloatField(null=True)
    Etapol = models.FloatField(null=True)
    Qcorr = models.FloatField(null=True)
    Cd = models.FloatField(null=True)
    Tau = models.FloatField(null=True)
    PisQcorr_ref = models.FloatField(null=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.entry_row.bsam_name}-{self.exit_row.bsam_name}"
        super().save(*args, **kwargs)

    def calculate_Qcorr(self, tau):
        self.Qcorr = self.Qcorr_ref * (tau ** 0.5) / self.Pi
        self.save()
        return self.Qcorr

    def calculate_pis_qcorr_ref(self):
        self.PisQcorr_ref = self.Pi / self.Qcorr_ref
        self.save()
        return self.PisQcorr_ref

    def is_only_stator(self):
        if self.entry_row.omega != 0.0 or self.exit_row.omega != 0.0:
            return False
        else:
            # To handle cases like RDE-RD8
            if self.entry_row.name != self.exit_row.name:
                return False
            else:
                return True


