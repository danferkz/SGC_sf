import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


'''
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'sql_formatter',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
    'formatters': {
        'sql_formatter': {
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s %(duration).3fms',
        },
    },
}




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda',
        'USER': 'postgres',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carpi',
        'USER': 'root',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '3306',
    }

}

'''

AUTH_USER_MODEL = 'users.CustomUser'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'users.CustomUser'


