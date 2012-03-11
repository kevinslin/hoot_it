from fabric.api import *
from fabric.contrib import console
from fabric.contrib.project import rsync_project
from fabric import utils

import os
import sys
try:
    fw_home = os.environ['FABRICW_HOME']
except KeyError:
    print ("you need to set FABRICW_HOME in your .bashrc")
    raise
sys.path.insert(0, fw_home)
from fabconf import fabconf


# Init
RSYNC_EXCLUDE = (
    '.DS_STORE',
    '.git',
    '*.pyc',
    'static/*',
    'fabfile.py',
)
env.key_filename = fabconf['SSH_PRIVATE_KEY_PATH']
env.environment = "production" # What is the produciton environmnet

def _setup_path():
    env.root = os.path.join(env.home, "webapps", "regen")

def staging():
    #CUSTOMIZE
    SERVER_HOST = "ec2-174-129-89-250.compute-1.amazonaws.com"
    env.home = "/home/ubuntu/"
    env.user = "ubuntu"
    env.hosts = [SERVER_HOST]
    _setup_path()

def production():
    utils.abort("Not yet implemented")

#def bootstrap():
    #"""
    #Initialize the virtualenv environment with django
    #"""
    #require('root', provided_by=('staging', 'production'))
    #run('mkdir -p %(root)s % env')
    #deploy()
    #update_requirements()

def update_requirements():
    pass

def deploy():
    """
    Rsync code to remote host
    """
    global RSYNC_EXCLUDE
    if env.environment == 'production':
        if not console.confirm('Are you sure you wnt to deploy?',
                                default = False):
            utils.abort('Production deployment aborted')
    extra_opts = "--omit-dir-times"
    rsync_project(
        remote_dir = env.root,
        local_dir = ".",
        exclude = RSYNC_EXCLUDE,
        delete = False,
        extra_opts = extra_opts
    )

### Local Methods

def migrate():
    """
    Do all neccessary migrations
    """
    local("python manage.py migrate userena")
    local("python manage.py migrate guardian")

def setup():
    """
    Setup after wipe
    """
    local("python manage.py check_permissions")



