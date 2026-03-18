# ruff: noqa: F403, F405

from .base import *

# Charger les variables d'environnement
SECRET_KEY = \
    "django-insecure-25yxc1w(%o!u=d$k8jt49odt@6#$td($6!=o!scik)stw-35w*"

DEBUG = True

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ["127.0.0.1"]

STATICFILES_DIRS = [
    "static",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "trunks-simu.db",
    }
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
LDAP_HOST = "ldaps://snm.snecma"
LDAP_DOMAIN = "SNM"
GROUP_OF_ALLOWED_USERS = "a0ykut01"


WORKING_REPERTORY = \
    r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\repertoire_de_travail"
