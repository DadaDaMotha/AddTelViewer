import os
from os import urandom
basedir = os.path.dirname(os.path.abspath(__file__))


dev_db_name = 'telscraper.db'

info_page_file = os.path.join(basedir, 'Documentation.md')
'''
app.config: In both cases (loading from any Python file or loading from modules),
    only uppercase keys are added to the config.  This makes it possible to use
    lowercase values in the config file for temporary values that are not added
    to the config or to define the config keys in the same file that implements
    the application.
'''

class Config(object):
    # DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = urandom(16)

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{}'.format(os.path.join(basedir, dev_db_name))


# Todo: Add environment variables
class ProductionConfig(Config):
    FLASK_ENV = 'production'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://telscraper:vood005643@postgres:5432/telscraper'

