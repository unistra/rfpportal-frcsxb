"""
Django settings for portal_frc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH,'templates')
STATIC_PATH = os.path.join(PROJECT_PATH,'static')

#DATABASE_PATH = os.path.join(PROJECT_PATH,'Union_1.db')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5q&kedarw39%0b)+x##@qunc5857oq@ln-#g96adw+q(ga9(w3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_profile',
    'rfp',
    'storages',
    'widget_tweaks',
    'bootstrap3',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#AUTH_USER_MODEL = 'user_profile.UserProfile'

ROOT_URLCONF = 'portal_frc.urls'

WSGI_APPLICATION = 'portal_frc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Parse database configuration from $DATABASE_URL

if os.getenv('DATABASE_URL'):
    DATABASES = {
                'default': {
                        'ENGINE': 'postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'd9pmli5c2jt4i6',                      # Or path to database file if using sqlite3.
                        #The following settings are not used with sqlite3:
                        'USER': 'qviasannlxqkov',
                        'PASSWORD': '3ZqmRyWulBDKf-mhIiJy-0OoEm',
                        'HOST': 'ec2-23-23-215-150.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '5432',
                }
            }

    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
else:
    DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'rfp_portal',                      # Or path to database file if using sqlite3.
                        #The following settings are not used with sqlite3:
                        'USER': 'postgres',
                        'PASSWORD': 'noosfere',
                        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '5433',
                }
    }

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#AWS configuration
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }

AWS_STORAGE_BUCKET_NAME = 'frcdev'
AWS_ACCESS_KEY_ID = 'AKIAJM2IT5AUXRQUPQJQ'
AWS_SECRET_ACCESS_KEY = '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'

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
#STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#MEDIA_ROOT = 'media'

MEDIA_ROOT = 'media'
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


if not os.getenv('DATABASE_URL'):
# Static asset configuration for local dev:
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'
    STATICFILES_LOCATION = 'static'

else:
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

STATICFILES_DIRS = (
        STATIC_PATH,
    )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

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

GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


