# -*- coding: utf-8 -*-

from os.path import abspath, basename, dirname, join, normpath


######################
# Path configuration #
######################

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)


#######################
# Debug configuration #
#######################

DEBUG = False
TEMPLATE_DEBUG = DEBUG


##########################
# Manager configurations #
##########################

WEBMASTER_MAIL = 'admin@icrfc.fr'

ADMINS = (
    ('Developer', 'sgug@outlook.com'),
    ('Webmaster', WEBMASTER_MAIL),
    ('Maintainer', 'ag@unistra.fr')
)

MANAGERS = ADMINS


##########################
# Database configuration #
##########################

# defaut db connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    },
    'django_explorer': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}


######################
# Site configuration #
######################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
LOGIN_REDIRECT_URL = "/user_profile/welcome/"


#########################
# General configuration #
#########################

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


#######################
# locale configuration #
#######################

LOCALE_PATHS = (normpath(join(SITE_ROOT, 'locale')),)


#######################
# Media configuration #
#######################

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

CUSTOM_MEDIA_STORAGE = False


##############################
# Static files configuration #
##############################

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/site_media/'

# Additional locations of static files
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

##############
# Secret key #
##############

# Make this unique, and don't share it with anybody.
# Only for dev and test environnement. Should be redefined for production
# environnement
SECRET_KEY = 'ma8r116)33!-#pty4!sht8tsa(1bfe%(+!&9xfack+2e9alah!'


##########################
# Template configuration #
##########################

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)


############################
# Middleware configuration #
############################

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'urlcrypt.auth_backends.UrlCryptBackend'
)

##########################
# Authentication Backends #
##########################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'urlcrypt.auth_backends.UrlCryptBackend',
)


#####################
# Url configuration #
#####################

ROOT_URLCONF = '%s.urls' % SITE_NAME


######################
# WSGI configuration #
######################

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME


#############################
# Application configuration #
#############################

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django_admin_bootstrapped',
    'django.contrib.admin'
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'widget_tweaks',
    'bootstrap3',
    'djrill',
    'import_export',
    'urlcrypt',
    'explorer',
    'django_wysiwyg',
    'django_comments',
    'django_extensions'
)

LOCAL_APPS = (
    'rfp',
    'user_profile'
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


#########################
# Session configuration #
#########################

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#######################
# Email configuration #
#######################

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
DEFAULT_FROM_EMAIL = WEBMASTER_MAIL

#####################
# Log configuration #
#####################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(name)s:%(lineno)s %(message)s'
         }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '',
            'maxBytes': 209715200,
            'backupCount': 3,
            'formatter': 'default'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO'
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rfp': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}

#############################
# Third party apps settings #
#############################

# django-sql-explorer
EXPLORER_CONNECTION_NAME = 'django_explorer'

# djrill
MANDRILL_API_KEY = ''

# urlcrypt
URLCRYPT_LOGIN_URL = '/user_profile/welcome/'

# bootstrapped admin configuration
from django.contrib import messages
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'
}

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

# django-wysiwyg
DJANGO_WYSIWYG_FLAVOR = "ckeditor"
DJANGO_WYSIWYG_MEDIA_URL = 'http://cdn.ckeditor.com/4.5.1/standard/ckeditor.js'
