from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UtilitaireConfiguration, RevueVeine

@receiver(user_logged_in)
def create_utilitaire_config(sender, request, user, **kwargs):
    if not UtilitaireConfiguration.objects.filter(user=user).exists():
        UtilitaireConfiguration.objects.create(
            user=user,
            genepi_path=r'C:\Appl\GENEPI\OPER\V3.4.6',
            cannelle_path=fr'C:\Users\{user}\Cannelle\OPER\CURRENT_V13R02\src',
            anNA_path=r'C:\Appl\AnNA\OPER\V1.9.0',
            carma_path=r'C:\SafApp\CARMA\Oper\LATEST_VERSION',
            ensight_path=r'C:\SafApp\ANSYS\v24r02-00\v242\CEI\bin\ensight242.bat',
        )


