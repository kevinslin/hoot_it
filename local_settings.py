import socket

DEBUG = False
TEMPLATE_DEBUG = DEBUG

#CUSTOMIZE
if socket.gethostname() == 'Maxwell.local':
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG


# Internationalization
LANGUAGE_CODE = 'en'
LANGUAGES = [('en', 'English'), ('de', 'German')]

# Debug Toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# Other
#CUSTOMIZE
#AUTH_PROFILE_MODULE = 'main.UserProfile'
