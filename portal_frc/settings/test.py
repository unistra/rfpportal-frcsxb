# -*- coding: utf-8 -*-

from .base import *

#######################
# Debug configuration #
#######################

DEBUG = True


##########################
# Database configuration #
##########################

DATABASES['default']['HOST'] = '{{ default_db_host }}'
DATABASES['default']['USER'] = '{{ default_db_user }}'
DATABASES['default']['PASSWORD'] = '{{ default_db_password }}'
DATABASES['default']['NAME'] = '{{ default_db_name }}'
DATABASES['django_explorer']['HOST'] = '{{ default_db_host }}'
DATABASES['django_explorer']['USER'] = '{{ django_explorer_db_user }}'
DATABASES['django_explorer']['PASSWORD'] = '{{ django_explorer_db_password }}'
DATABASES['django_explorer']['NAME'] = '{{ default_db_name }}'


############################
# Allowed hosts & Security #
############################

ALLOWED_HOSTS = [
    '.u-strasbg.fr',
    '.unistra.fr',
    '.icrfc.fr',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'ssl')


#####################
# Log configuration #
#####################

LOGGING['handlers']['file']['filename'] = '{{ remote_shared_path }}/log/app.log'
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['level'] = 'DEBUG'

##############
# Secret key #
##############

SECRET_KEY = '{{ secret_key }}'


############
# Mandrill #
############

MANDRILL_API_KEY = '{{ mandrill_api_key }}'
