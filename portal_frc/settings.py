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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']



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
    'rfp',
    'storages',
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

    #AWS configuration
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    #Email configuration
    MANDRILL_API_KEY = os.getenv('MANDRILL_API_KEY')

    # Static asset configuration for hosted dev:
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


else:
    #SQL-explorer setting
    # SECRET_KEY = api_key.SECRET_KEY
    DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'rfpportal-dev',                      # Or path to database file if using sqlite3.
                        #The following settings are not used with sqlite3:
                        'USER': 'admindip',
                        'PASSWORD': 'woopei7U',
                        'HOST': 'bddrfpportal-dev.u-strasbg.fr',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                        'PORT': '5432',
                },
                'django_explorer': {
                            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                            'NAME': 'rfpportal-dev',                      # Or path to database file if using sqlite3.
                            #The following settings are not used with sqlite3:
                            'USER': 'rfpportal-dev',
                            'PASSWORD': 'Eixu1ier',
                            'HOST': 'bddrfpportal-dev.u-strasbg.fr',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                            'PORT': '5432',
                    }
    }

    #AWS configuration
    #AWS_STORAGE_BUCKET_NAME = api_key.AWS_STORAGE_BUCKET_NAME
    # AWS_ACCESS_KEY_ID = api_key.AWS_ACCESS_KEY_ID
    # AWS_SECRET_ACCESS_KEY = api_key.AWS_SECRET_ACCESS_KEY
    # AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    #Email configuration
    # MANDRILL_API_KEY = api_key.MANDRILL_API_KEY

    # Static asset configuration for local dev:
    STATIC_ROOT = os.path.join(PROJECT_PATH, 'assets')
    STATIC_URL = '/static/'
    STATICFILES_LOCATION = 'static'



# Media files configuration
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
CUSTOM_MEDIA_STORAGE = True

