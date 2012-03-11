import socket

DEBUG = True
TEMPLATE_DEBUG = True

#CUSTOMIZE
if socket.gethostname() == 'Maxwell.local':
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG


# Internationalization
LANGUAGE_CODE = 'en'
LANGUAGES = [('en', 'English')]

# Debug Toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# Other
#CUSTOMIZE
#AUTH_PROFILE_MODULE = 'main.UserProfile'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'simple':{
            'format': ('%(name)s: [%(levelname)s] %(message)s'),
        },
        'verbose':{
            'format': ('%(name)s: [[%(levelname)s]-%(asctime)s-%(module)s.py:%(funcName)s: %(message)s'),
            'datefmt':'%H:%m:%S',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console_s':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'simple'
        },
        'console_v':{
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
        'django.console':{
            'handlers': ['console_s'],
            'level':'DEBUG',
        },
        'django.simplelogger_s':{
            'handlers':['console_s'],
            'level': 'DEBUG'
        },
        'django.simplelogger_v':{
            'handlers':['console_v'],
            'level': 'DEBUG'
        }
    }
}

