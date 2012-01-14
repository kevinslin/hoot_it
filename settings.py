import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
     ('Kevin S Lin', 'kevinslin8@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, "data.sql"),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    # Optional
    'sekizai.context_processors.sekizai',
    'navbar.context_processors.navbars',

)

TIME_ZONE = 'America/Chicago'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "assets"),
    os.path.join(PROJECT_ROOT, "assets", "jquery"),
    os.path.join(PROJECT_ROOT, "assets", "core"),
    os.path.join(PROJECT_ROOT, "assets", "custom"),
    os.path.join(PROJECT_ROOT, "assets", "contrib"),
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '9%)xh35t1(#worul6f3gw_v_4@=-i&ilqze7lzv^d1ny13nqjt'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Extra
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Custom
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


ROOT_URLCONF = 'prototype.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Extra
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    # View
    'sekizai',

    # Inital
    'bond',
    'main',

    # Optional
    'navbar',

    #Development
    'south',
    'django_extensions',
    'debug_toolbar',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'simple':{
            'format': ('[%(levelname)s]: %(message)s'),
        },
        'verbose':{
            'format': ('[%(levelname)s] %(asctime)s %(module)s: %(message)s'),
            'datefmt':'%H:%m:%S',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.custom':{
            'handlers': ['console'],
            'level':'DEBUG',
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
