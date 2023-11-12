from pathlib import Path
import io
import os
from functools import lru_cache
from decouple import Config, RepositoryEmpty, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR.parent / ".env"


class RepositoryString(RepositoryEmpty):
    def __init__(self, source):
        source = io.StringIO(source)
        if not isinstance(source, io.StringIO):
            raise ValueError("source must be an instance of io.StringIO")
        self.data = {}
        file_ = source.read().split("\n")
        for line in file_:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip()
            if len(v) >= 2 and (
                (v[0] == "'" and v[-1] == "'") or (v[0] == '"' and v[-1] == '"')
            ):
                v = v[1:-1]
            self.data[k] = v

    def __contains__(self, key):
        return key in os.environ or key in self.data

    def __getitem__(self, key):
        return self.data[key]


@lru_cache()
def get_config():
    if ENV_PATH.exists():
        return Config(RepositoryEnv(str(ENV_PATH)))
    from decouple import config

    return config


config = get_config()

SECRET_KEY = config("SECRET_KEY", cast=str)
DEBUG = config("DEBUG", cast=bool, default=True)

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "static/media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
WSGI_APPLICATION = "digitalmarketplace.wsgi.application"

SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'    # pals?

ALLOWED_HOSTS = ['*']

params = {
    "database": config("DATABASE_NAME", cast=str),
    "user": config("DATABASE_USER", cast=str),
    "password": config("DATABASE_PASS", cast=str),
    "host": config("DATABASE_HOST", cast=str),
    "port": config("DATABASE_PORT", cast=int),
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "admin_honeypot",
    "_account", # App
    "_store",   # App
    "_cart",    # App
    "_payment", # App
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "digitalmarketplace.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                '_store.views.categories',
                '_cart.context_processors.cart',
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgres": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": params["database"],
        "USER": params["user"],
        "PASSWORD": params["password"],
        "HOST": params["host"],
        "PORT": params["port"],
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = 'True'

EMAIL_HOST_USER = config("E_HOST_USER", cast=str, default='')
EMAIL_HOST_PASSWORD = config("E_HOST_PASSWORD", cast=str, default='')