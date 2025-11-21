# ruff: noqa: F403, F405

from .base import *

# SECRET_KEY = get_env("SAFRANAE_DJANGO_SECRET_KEY")
SECRET_KEY = "25yxc1w(%o!u=d$k8jt49odt@6#$td($6!=o!scik)stw-35w*"

DEBUG = True

ALLOWED_HOSTS = ["*"]

WORKING_REPERTORY = \
    r"\\nas23\YRKC\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\03_Postprocessing\TRUNKS\data\repertoire_de_travail"

EXCEL_POST_ANNA_PATH = r"post\postAnNA\Perfos0D_moy_7.xlsx"
EXCEL_POST_ANTARES_PATH = r"post\postAntares\Perfos0D_moy_7.xlsx"
HDF5_PATH = r"post\postAnNA\Gradients_Complets.trac"
BSAM_PATH = r"init\bc_BSAM"
PERFOS0D_EXPORT_NAME = "export_perfos0D"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "trunks-simu",
    }
}


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "bootstrap5",
    'apps.main',  # Add this line
    "django_login",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# LDAP UtilitaireConfiguration
AUTHENTICATION_BACKENDS = [
    "src.config.ldapauthbackend.LdapAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]
# LDAP_HOST = get_env("LDAP_HOST")
# LDAP_DOMAIN = get_env("LDAP_DOMAIN")
# GROUP_OF_ALLOWED_USERS = get_env("GROUPE_RUG")

LDAP_HOST = "ldaps://snm.snecma"
LDAP_DOMAIN = "SNM"
GROUP_OF_ALLOWED_USERS = "a0ykut01"

# Authentication
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
