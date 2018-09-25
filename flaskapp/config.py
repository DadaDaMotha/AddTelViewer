import os
from os import urandom
basedir = os.path.split(os.path.realpath(__file__))[0]


'''
app.config: In both cases (loading from any Python file or loading from modules),
    only uppercase keys are added to the config.  This makes it possible to use
    lowercase values in the config file for temporary values that are not added
    to the config or to define the config keys in the same file that implements
    the application.
'''

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = urandom(16)

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False



