"""
Django settings for terra project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


def get_allowed_hosts():
    """
    Get allowed hosts from .env file

    If DEBUG = True and ALLOWED_HOSTS is empty or null,
    default to ['.dymaxionlabs.com']

    """
    hosts = [s for s in os.getenv('ALLOWED_HOSTS', '').split(',') if s]
    if not DEBUG and not hosts:
        hosts = ['.dymaxionlabs.com']
    return hosts


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv('DEBUG', 0)) > 0

ALLOWED_HOSTS = get_allowed_hosts()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    'projects.apps.ProjectsConfig',
    'quotations.apps.QuotationsConfig',
    'tasks.apps.TasksConfig',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
    'corsheaders',
    'anymail',
    'drf_yasg',
    'jsoneditor',
    'guardian',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'terra.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'global_settings': 'terra.templatetags.global_settings',
            }
        },
    },
]

WSGI_APPLICATION = 'terra.wsgi.application'

# Emails

ANYMAIL = {
    'MAILGUN_API_KEY': os.getenv('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': os.getenv('MAILGUN_SENDER_DOMAIN'),
}

# In production, add this to your .env:
#   EMAIL_BACKEND=anymail.backends.mailgun.EmailBackend
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND',
                          'django.core.mail.backends.console.EmailBackend')

DEFAULT_FROM_EMAIL = 'Terra <{email}>'.format(
    email=os.getenv('DEFAULT_FROM_EMAIL'))

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates', 'static')]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer', ),
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('terra.authentication.TokenAuthentication', ),
    'DEFAULT_PERMISSION_CLASSES':
    ('rest_framework.permissions.IsAuthenticated', ),
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':
    25
}

# Allow all domains
CORS_ORIGIN_ALLOW_ALL = True

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

SITE_ID = 1

ACCOUNT_ADAPTER = 'terra.adapter.DefaultAccountAdapterCustom'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
MEDIA_URL = '/uploads/'

FILES_BUCKET = os.getenv('FILES_BUCKET')
TILES_BUCKET = os.getenv('TILES_BUCKET')

WEBCLIENT_URL = os.getenv('WEBCLIENT_URL')

# For images and other uploaded files
# In production, add this to your .env:
#   DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
DEFAULT_FILE_STORAGE = os.getenv(
    'DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')

GS_BUCKET_NAME = FILES_BUCKET

# Configure Sentry
if os.environ['SENTRY_DNS']:
    sentry_sdk.init(
        dsn=os.environ['SENTRY_DNS'], integrations=[DjangoIntegration()])

CELERY_RESULT_BACKEND = 'tasks.backends.DatabaseBackend'

# Path to directory that holds temporary raster/vector tiles
TILES_DIR = os.path.join(BASE_DIR, 'tiles')
