import os
from os import urandom

BASEDIR = os.path.dirname(os.path.abspath(__file__))
APPS_DIR = os.path.join(BASEDIR, 'SinglePageDashApps')

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
FLASK_ENV = os.environ.get('FLASK_ENV')
DB_BACKEND = os.environ.get('DB_BACKEND')

STATIC_ROOT = '/var/www/static'

if DB_BACKEND == 'postgres':
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@postgres:5432/{DB_NAME}'
else:
    SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.path.join(BASEDIR, "default.db")}'

class Config:
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = urandom(16)
    FLASK_ENV = FLASK_ENV
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
