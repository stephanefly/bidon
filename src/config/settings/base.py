"""
Module settings de base.
"""
import os
from pathlib import Path
import sys

from django.core.exceptions import ImproperlyConfigured
from yaml import safe_load

# Initialize environment variables
BASE_DIR = Path(__file__).resolve().parent.parent.parent

IS_WINDOWS = (os.name == "nt")   # nt = Windows, posix = Linux/Mac
PATH_STYLE = "windows" if IS_WINDOWS else "linux"

try:
    ENV_FILEPATH = os.environ["ENV_FILEPATH"]
except KeyError:
    ENV_FILEPATH = os.path.join(BASE_DIR, ".env")
try:
    with open(ENV_FILEPATH) as f:
        loaded_env = safe_load(f)
except FileNotFoundError:
    loaded_env = None


def get_env(key, env_variables=loaded_env):
    try:
        if env_variables:
            return env_variables[key]
        return os.environ[key]
    except KeyError:
        error_msg = f"{key} env variable not found !"
    raise ImproperlyConfigured(error_msg)


ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "bootstrap5",
    "apps.main",
    "django_login",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'apps.main.middlewares.TimerMiddleware',  # Ajouter le middleware
]

ROOT_URLCONF = "config.urls"
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

WSGI_APPLICATION = "config.wsgi.application"

# Database Configuration for SQLite3
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        # Place the database file in the project base directory
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "fr-FR"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LDAP Configuration
AUTHENTICATION_BACKENDS = [
    "django_login.ldapauthbackend.LdapAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]



# Authentication
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
GROUP_OF_ALLOWED_USERS = 'a0ykut01'
GROUP_OF_STAFF_USERS = 'a0ykut01'
GROUP_OF_SUPERUSERS = 'a0ykut01'
LDAP_HOST = r"ldaps://one.ad"
LDAP_DOMAIN = "one"
LDAP_SERVER = "one.ad"

PROJECT_NAME = "Trunks"
LOGIN_MESSAGE = "Bienvenue sur Trunks"

# RGPD / Mode sombre
COMPLIANCE_MODE = True
RETENTION_DAYS = 10
LOGGING_DARK_MODE = False

EXCEL_POST_ANNA_PATH_7 = r"post\postAnNA\Perfos0D_moy_7.xlsx"
EXCEL_POST_ANTARES_PATH_7 = r"post\postAntares\Perfos0D_moy_7.xlsx"
EXCEL_POST_ANNA_PATH_10 = r"post\postAnNA\Perfos0D_moy_10.xlsx"
EXCEL_POST_ANTARES_PATH_10 = r"post\postAntares\Perfos0D_moy_10.xlsx"
HDF5_PATH = r"post\postAnNA\Gradients_Complets.trac"
BSAM_PATH = r"init\bc_BSAM"
PERFOS0D_EXPORT_NAME = "export_perfos0D"
WORKING_REPERTORY = \
    r"\\data\_R_et_T\H7-MAORI\DTP-1\Veine\Calculs\RM9_RD9\TOUT\TEST-TRUNKS"