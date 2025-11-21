
from django import forms
from .models import ProjetShenron
from .models import Etat, Project, RevueVeine, UtilitaireConfiguration, RevueAube, Aube


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]


class RevueVeineForm(forms.ModelForm):
    class Meta:
        model = RevueVeine
        fields = ["name"]


class RevueAubeForm(forms.ModelForm):
    class Meta:
        model = RevueAube
        fields = ["name", "dico_genepi_auto"]


class EtatForm(forms.ModelForm):
    class Meta:
        model = Etat
        fields = ["name"]


class ConfigurationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # récupère l'utilisateur passé depuis la vue
        super().__init__(*args, **kwargs)

        if user:
            login = user.username  # ou user.get_username() selon votre config LDAP
            self.fields['cannelle_path'].initial = fr'C:\Users\{login}\Cannelle\OPER\CURRENT_V13R02\src'

    class Meta:
        model = UtilitaireConfiguration
        exclude = ['user']  # Liste des champs à exclure


        widgets = {
            'genepi_path': forms.TextInput(attrs={
                'placeholder': r'Exemple : C:\Appl\GENEPI\OPER\V3.4.6',
                'value': r'C:\Appl\GENEPI\OPER\V3.4.6',
                'style': 'width: 100%; padding: 12px; font-size: 16px; border-radius: 6px; border: 1px solid #ccc;'
            }),
            'cannelle_path': forms.TextInput(attrs={
                'placeholder': r'Exemple : C:\Appl\GENEPI\OPER\V3.4.6',
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
            'ensight_path': forms.TextInput(attrs={
                'type': 'hidden',
            }),
            'genepi_auto_path': forms.TextInput(attrs={
                'placeholder': r'Exemple : C:\SafApp\DARIUS\Script_DARIUS_24.03.27\Scripts\Scripts_Outils\GENEPI\GENEPIAuto.py',
                'value': r'C:\SafApp\DARIUS\Script_DARIUS_24.03.27\Scripts\Scripts_Outils\GENEPI\GENEPIAuto.py',
                'style': 'width: 100%; padding: 12px; font-size: 16px; border-radius: 6px; border: 1px solid #ccc;'
            }),
        }


class AubeForm(forms.ModelForm):
    class Meta:
        model = Aube
        fields = "__all__"
        exclude = ("revue_aube",)
    def clean_fichier_bsam(self):
        val = self.cleaned_data.get("fichier_bsam", "")
        return val.replace('"', '').strip()

    def clean_lien_xml(self):
        val = self.cleaned_data.get("lien_xml", "")
        return val.replace('"', '').strip()



class ProjetShenronForm(forms.ModelForm):
    class Meta:
        model = ProjetShenron
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
