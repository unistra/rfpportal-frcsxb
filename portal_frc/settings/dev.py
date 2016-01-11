# -*- coding: utf-8 -*-

from os import environ
from os.path import normpath
from .base import *

#######################
# Debug configuration #
#######################

DEBUG = True


##########################
# Database configuration #
##########################

DATABASES['default']['HOST'] = environ.get('DEFAULT_DB_HOST',
                                           'bddrfpportal-dev.u-strasbg.fr')
DATABASES['default']['USER'] = environ.get('DEFAULT_DB_USER')
DATABASES['default']['PASSWORD'] = environ.get('DEFAULT_DB_PASSWORD')
DATABASES['default']['NAME'] = environ.get('DEFAULT_DB_NAME', 'rfpportal-dev')
DATABASES['django_explorer']['HOST'] = DATABASES['default']['HOST']
DATABASES['django_explorer']['USER'] = environ.get('EXPLORER_DB_USER')
DATABASES['django_explorer']['PASSWORD'] = environ.get('EXPLORER_DB_PASSWORD')
DATABASES['django_explorer']['NAME'] = DATABASES['default']['NAME']


#####################
# Log configuration #
#####################

LOG_DIR = '/tmp'

LOGGING['handlers']['file']['filename'] = normpath(join(LOG_DIR, '%s.log' % SITE_NAME))
LOGGING['handlers']['file']['level'] = 'DEBUG'

for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['level'] = 'DEBUG'


###########################
# Unit test configuration #
###########################

INSTALLED_APPS += (
    'debug_toolbar',
)

#################
# Debug toolbar #
#################

DEBUG_TOOLBAR_PATCH_SETTINGS = False
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0')

#######################
# Email configuration #
#######################
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = normpath(join(LOG_DIR, '%s_mails.log' % SITE_NAME))
EMAIL_HOST = 'localhost'

