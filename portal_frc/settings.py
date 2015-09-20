"""
Django settings for portal_frc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

if not os.getenv('DATABASE_URL'):
    from keys.keys import api_key

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH,'templates')
STATIC_PATH = os.path.join(PROJECT_PATH,'static')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ADMIN = (('Developer', 'sgug@outlook.com'), ('Webmaster', 'admin@icfrc.fr'))

# Application definition
INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'user_profile',
    'rfp',
    'widget_tweaks',
    'bootstrap3',
    'djrill',
    'import_export',
    'urlcrypt',
    'explorer',
    'django_wysiwyg',
    'django_comments',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'urlcrypt.auth_backends.UrlCryptBackend',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'urlcrypt.auth_backends.UrlCryptBackend',
)

ROOT_URLCONF = 'portal_frc.urls'

WSGI_APPLICATION = 'portal_frc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Parse database configuration from $DATABASE_URL

if os.getenv('DATABASE_URL'):

    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASES = {
                'default': {
                        'ENGINE': 'postgresql_psycopg2',                       # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': os.getenv('DB_NAME'),                          # Or path to database file if using sqlite3.
                                                                               #The following settings are not used with sqlite3:
                        'USER': os.getenv('DB_USER'),
                        'PASSWORD': os.getenv('DB_PWD'),
                        'HOST': 'ec2-23-23-215-150.compute-1.amazonaws.com',   # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '5432',
                }
            }

    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

    #Email configuration
    MANDRILL_API_KEY = os.getenv('MANDRILL_API_KEY')
    EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
    DEFAULT_FROM_EMAIL = 'admin@icfrc.fr'



else:
    #SQL-explorer setting
    EXPLORER_CONNECTION_NAME = 'django_explorer'
    SECRET_KEY = api_key.SECRET_KEY
    DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'rfp_portal_2',                      # Or path to database file if using sqlite3.
                        #The following settings are not used with sqlite3:
                        'USER': 'postgres',
                        'PASSWORD': 'noosfere',
                        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '5433',
                },
                'django_explorer': {
                            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                            'NAME': 'rfp_portal_2',                      # Or path to database file if using sqlite3.
                            #The following settings are not used with sqlite3:
                            'USER': 'django_explorer',
                            'PASSWORD': 'noosfere',
                            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                            'PORT': '5433',
                    }
    }

    #Email configuration
    MANDRILL_API_KEY = api_key.MANDRILL_API_KEY
    EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
    DEFAULT_FROM_EMAIL = 'contact@icfrc.fr'

# Static asset configuration for local dev:
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_LOCATION = 'static'

STATICFILES_DIRS = (
       STATIC_PATH,
)

# Media files configuration
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS=(
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

#urlcrypt settings
URLCRYPT_LOGIN_URL = '/user_profile/welcome/'

#Boostrapped Admin Config.
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

#Django-wysiwyg Config.
DJANGO_WYSIWYG_FLAVOR = "ckeditor"
DJANGO_WYSIWYG_MEDIA_URL = 'http://cdn.ckeditor.com/4.5.1/standard/ckeditor.js'

from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

LOGIN_REDIRECT_URL = "/user_profile/welcome/"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers' : {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },

    'loggers':{
        'rfp.views': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}