
from django import forms
from apps.main.utils.paths import normalize_path_os, clean_user_ihm_path
from .models import (
    Aube,
    Etat,
    Project,
    ProjetShenron,
    RevueAube,
    RevueVeine,
    UtilitaireConfiguration,
)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"autofocus": "autofocus"})
        }

class RevueVeineForm(forms.ModelForm):
    class Meta:
        model = RevueVeine
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"autofocus": "autofocus"})
        }


class RevueAubeForm(forms.ModelForm):
    class Meta:
        model = RevueAube
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"autofocus": "autofocus"})
        }


class EtatForm(forms.ModelForm):
    class Meta:
        model = Etat
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"autofocus": "autofocus"})
        }

class ConfigurationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # récupère l'utilisateur passé depuis la vue
        super().__init__(*args, **kwargs)

        if user:
            login = user.username  # ou user.get_username() selon votre config LDAP
            self.fields['cannelle_path'].initial = fr'C:\Users\{login}\Cannelle\OPER\CURRENT_V13R02\src'

    def clean_user_directory(self):
        path = self.cleaned_data.get('user_directory')

        if not path:
            return path

        # Conversion Windows -> Unix
        path = str(path).strip()
        path = path.replace("\\", "/")

        # Forcer UNC Linux : \\data -> //data
        if path.startswith("/data"):
            path = "/" + path
        elif path.startswith("//data") is False and path.startswith("data") is False:
            if path.startswith("/"):
                path = "/" + path
            else:
                path = "//" + path

        return path

    class Meta:
        model = UtilitaireConfiguration
        exclude = ['user']  # Liste des champs à exclure

        widgets = {
            'genepi_path': forms.TextInput(attrs={
                'placeholder': r'Exemple : C:\Appl\GENEPI\OPER\V3.5.4',
                'value': r'C:\Appl\GENEPI\OPER\V3.4.6',
                'style': 'width: 100%; padding: 12px; font-size: 16px; border-radius: 6px; border: 1px solid #ccc;'
            }),
            'cannelle_path': forms.TextInput(attrs={
                'placeholder': r'Exemple : C:\Users\sXXXXXX\Cannelle\OPER\CURRENT_V13R05\src',
                'style': 'width: 100%; padding: 12px; font-size: 16px; border-radius: 6px; border: 1px solid #ccc;'
            }),
            'anNA_path': forms.TextInput(attrs={
                'placeholder': r'Exemple : C:\Appl\AnNA\OPER\V1.9.0',
                'value': r'C:\Appl\AnNA\OPER\V1.9.0',
                'style': 'width: 100%; padding: 12px; font-size: 16px; border-radius: 6px; border: 1px solid #ccc;'
            }),
            'carma_path': forms.TextInput(attrs={
                'placeholder': r'Exemple : C:\SafApp\CARMA\Oper\LATEST_VERSION',
                'value': r'C:\SafApp\CARMA\Oper\LATEST_VERSION',
                'style': 'width: 100%; padding: 12px; font-size: 16px; border-radius: 6px; border: 1px solid #ccc;'
            }),
            'user_directory': forms.TextInput(attrs={
                'placeholder': r'Exemple : \\data\_R_et_T\H7-MAORI\DTP-1\Veine\Calculs\Scripts\TRUNKS',
                'value': r'',
                'style': 'width: 100%; padding: 12px; font-size: 16px; border-radius: 6px; border: 1px solid #ccc;'
            }),
            'ensight_path': forms.TextInput(attrs={
                'type': 'hidden',
            }),
            'genepi_auto_path': forms.TextInput(attrs={
                'type': 'hidden',
            }),
        }


class AubeForm(forms.ModelForm):
    class Meta:
        model = Aube
        fields = "__all__"
        exclude = ("revue_aube", "used")

        widgets = {
            "projet": forms.TextInput(attrs={
                "placeholder": "Exemple: CME3"
            }),
            "version": forms.TextInput(attrs={
                "placeholder": "Exemple: S1"
            }),
            "aube": forms.TextInput(attrs={
                "placeholder": "Exemple: S1AB"
            }),
            "type_coupe_nbre_ldc": forms.TextInput(attrs={
                "placeholder": "Exemple: CQ"
            }),
            "coupe_dessin": forms.TextInput(attrs={
                "placeholder": "Exemple: 1,11,15,19,29"
            }),
            "label_bsam": forms.TextInput(attrs={
                "placeholder": "Exemple: S1"
            }),
            "calage_deg": forms.NumberInput(attrs={
                "placeholder": "Exemple: 0.0",
                "step": "0.01"
            })
        }


    def clean_fichier_bsam(self):
        val = self.cleaned_data.get("fichier_bsam", "")
        cleaned_val = clean_user_ihm_path(val)
        return normalize_path_os(cleaned_val)

    def clean_lien_xml(self):
        val = self.cleaned_data.get("lien_xml", "")
        cleaned_val = clean_user_ihm_path(val)
        return normalize_path_os(cleaned_val)



class ProjetShenronForm(forms.ModelForm):
    class Meta:
        model = ProjetShenron
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "autofocus": "autofocus"}),
        }
