# ruff: noqa: F403, F405

from .base import *

# Charger les variables d'environnement
SECRET_KEY = \
    "django-insecure-25yxc1w(%o!u=d$k8jt49odt@6#$td($6!=o!scik)stw-35w*"

DEBUG = True

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ["127.0.0.1"]

WORKING_REPERTORY = \
    r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\repertoire_de_travail"

EXCEL_POST_ANNA_PATH_7 = r"post\postAnNA\Perfos0D_moy_7.xlsx"
EXCEL_POST_ANNA_PATH_10 = r"post\postAnNA\Perfos0D_moy_10.xlsx"
EXCEL_POST_ANTARES_PATH_7 = r"post\postAntares\Perfos0D_moy_7.xlsx"
EXCEL_POST_ANTARES_PATH_10 = r"post\postAntares\Perfos0D_moy_10.xlsx"

HDF5_PATH = r"post\postAnNA\Gradients_Complets.trac"
BSAM_PATH = r"init\bc_BSAM"

PERFOS0D_EXPORT_NAME = "export_perfos0D"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "trunks-simu.db",
    }
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
LDAP_HOST = "ldaps://snm.snecma"
LDAP_DOMAIN = "SNM"
GROUP_OF_ALLOWED_USERS = "a0yycu03"

INSTALLED_APPS += ['silk']
MIDDLEWARE += ['silk.middleware.SilkyMiddleware']
