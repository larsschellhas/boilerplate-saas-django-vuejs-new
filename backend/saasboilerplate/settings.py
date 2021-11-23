"""
Django settings for saasboilerplate project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Setup allowed hosts with the defined environmental variable if existing
ALLOWED_HOSTS = [env("WEBSITE_HOSTNAME")] if "WEBSITE_HOSTNAME" in env.ENVIRON else []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "django_drf_filepond",
    "cuser",
    "usermanagement",
    "corsheaders",
    "django_extensions",
    "djmoney",
    "drf_app_generators",
    "rest_framework_simplejwt",
    "django_rest_passwordreset",
    "djstripe",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "saasboilerplate.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "saasboilerplate.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# REST Framework

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.DjangoModelPermissions"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 50,
}


# Cross Origin Handling
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('content-disposition', 'accept-encoding',
                      'content-type', 'accept', 'origin', 'authorization')


# Filepond configuration
DJANGO_DRF_FILEPOND_UPLOAD_TMP = os.path.join(
    BASE_DIR, 'filepond-temp-uploads')
DJANGO_DRF_FILEPOND_FILE_STORE_PATH = os.path.join(BASE_DIR, 'filepond-stored-uploads')


# Custom User Model
AUTH_USER_MODEL = "usermanagement.User"


# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}
DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE = True


# Emails are send to the console, if an email server is not defined through environmental variables
if "EMAIL_BACKEND" in env.ENVIRON and "EMAIL_HOST" in env.ENVIRON and "EMAIL_PORT" in env.ENVIRON and "EMAIL_USE_TLS" in env.ENVIRON and "EMAIL_HOST_USER" in env.ENVIRON and "EMAIL_HOST_PASSWORD" in env.ENVIRON:
    EMAIL_BACKEND = env('EMAIL_BACKEND')
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS', bool)
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    SERVER_EMAIL = env('EMAIL_FROM')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


### Settings for customization
# Enter the name of your site. It will be used, e.g., in emails
SITE_NAME = 'SimplySaaS'
# URLs to your frontend (with trailing slash '/' )
FRONTEND_URL = 'https://localhost:8080/'
# URL to your frontend page where users can reset their password
FRONTEND_RESET_PASSWORD_PATH = 'login/reset/'


### Stripe configuration
STRIPE_LIVE_SECRET_KEY = env("STRIPE_LIVE_SECRET_KEY")
STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY")
STRIPE_LIVE_MODE = False
# Get your webhook secret from the section in the Stripe dashboard where you added the webhook endpoint
DJSTRIPE_WEBHOOK_SECRET = env("DJSTRIPE_WEBHOOK_SECRET")
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
