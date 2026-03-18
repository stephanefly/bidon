# ruff: noqa: F403, F405

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env("SAFRANAE_DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = Path(__file__).resolve().parents[2]


ALLOWED_HOSTS = get_env("SAFRANAE_ALLOWED_HOSTS").split(",")

CSRF_TRUSTED_ORIGINS = get_env("SAFRANAE_CSRF_TRUSTED_ORIGINS").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": get_env("SAFRANAE_DB_HOST"),
        "NAME": get_env("SAFRANAE_DB_NAME"),
        "USER": get_env("SAFRANAE_DB_USERNAME"),
        "PASSWORD": get_env("SAFRANAE_DB_PASSWORD"),
    }
}

ADMINS = []

FORCE_SCRIPT_NAME = "/trunks"

STATIC_URL = FORCE_SCRIPT_NAME + "/static/"
STATIC_ROOT = get_env("SAFRANAE_STATIC_ROOT")



MEDIA_ROOT = get_env("SAFRANAE_MEDIA_ROOT")
MEDIA_URL = FORCE_SCRIPT_NAME + "/media/"


LOGIN_URL = FORCE_SCRIPT_NAME + '/login/'
LOGIN_REDIRECT_URL = FORCE_SCRIPT_NAME + '/'
LOGOUT_REDIRECT_URL = FORCE_SCRIPT_NAME + '/'

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "bootstrap5",
    "apps.main",  # Correction ici
    "django_login",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "apps" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_login.context_processors.project_name",
                "django_login.context_processors.login_message",
                "django_login.context_processors.compliance_mode",
                "django_login.context_processors.retention_days",
                "django_login.context_processors.show_ldap_login_button",
            ],
        },
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} - {levelname} - {name} - {module} - {message}",
            "style": "{",
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": get_env("SAFRANAE_LOGGING_FILENAME"),
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "trunks": {
            "handlers": ["file"],
            "level": "INFO",
            "filters": [],
        },
    },
}


EXCEL_POST_ANNA_PATH_7 = r"post/postAnNA/Perfos0D_moy_7.xlsx"
EXCEL_POST_ANTARES_PATH_7 = r"post/postAntares/Perfos0D_moy_7.xlsx"
EXCEL_POST_ANNA_PATH_10 = r"post/postAnNA/Perfos0D_moy_10.xlsx"
EXCEL_POST_ANTARES_PATH_10 = r"post/postAntares/Perfos0D_moy_10.xlsx"
HDF5_PATH = r"post/postAnNA/Gradients_Complets.trac"
BSAM_PATH = r"init/bc_BSAM"
PERFOS0D_EXPORT_NAME = "export_perfos0D"

WORKING_REPERTORY = r"//data/_R_et_T/H7-MAORI/DTP-1/Veine/Calculs/RM9_RD9/TOUT/TEST-TRUNKS"