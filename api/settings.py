# -*- coding:utf-8 -*-
"""
Django settings for api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import pymongo


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7$-u-^f+yz)v$h3y@m9fsz_7#ym6s-e!r_z5bq^4i+7jo!4^d6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = []

APPEND_SLASH = False

TEMPLATE_CONTEXT_PROCESSORS = (

    "django.contrib.auth.context_processors.auth",
    # "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    # "django.core.context_processors.csrf",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # "django.core.context_processors.request",
)

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    # "django.template.loaders.eggs.Loader",
    # "django.template.loaders.cached.Loader",
    "django.template.loaders.app_directories.Loader",
)

# TEMPLATE_LOADERS = (
#     ('django.template.loaders.cached.Loader', (
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#         )
#     ),
# )

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    # 'rest_framework',
    # 'restful.authtoken',
    'restful',
    'openstack',
    'public',
    'alipay',
    'css',
    'angularjs',
    'nodejs',
    'bootstrap',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/jquery-1.9.1.min.js',
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'restful.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ROOT_URLCONF = 'api.urls'

WSGI_APPLICATION = 'api.wsgi.application'

# login url

LOGIN_URL = ''

# restful_dir
RESTFUL_DIR = (os.path.join(BASE_DIR, 'restful'))

# settings templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# settings dababases dir

DATABASE_DIR = (
    os.path.join(BASE_DIR, 'db')
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '192.168.30.124',
        'NAME': 'xcloud_db',
        'USER': 'eclouduser',
        'PASSWORD': 'eclouduser123',
        'PORT': '3306',
    }
}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATABASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = (
    ('en-us', 'English'),
    ('zh-cn', 'Simplified Chinese'),
    ('zh-tw', 'Traditional Chinese'),
)

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# LOGIN_URL =''

# MEDIA_ROOT = ''

# MEDIA_URL = ""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR + '/logs/', 'all.log'),  # 或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR + '/logs/', 'request.log'),  # 或者直接写路径：'filename':'c:\logs\request.log''
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'response_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR + '/logs/', 'response.log'),  # 或者直接写路径：'filename':'c:\logs\request.log''
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR + '/logs/', 'script.log'),  # 或者直接写路径：'filename':'c:\logs\script.log'
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        'django.response': {
            'handlers': ['default', 'response_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'public.app': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'openstack.app': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'scripts': {  # 脚本专用日志
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
mongo_conn = pymongo.MongoClient("192.168.30.124", 27017)
