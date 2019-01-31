import os
from .utils.io import cat

BASEDIR = os.path.dirname(os.path.abspath(__file__))
APP_NAME = os.path.split(BASEDIR)[-1]

TEMPLATE_DIR = os.path.join(BASEDIR, 'templates')
REACT_WRAPPER = os.path.join(TEMPLATE_DIR, 'main_wrapper.html')
STATIC_FOLDER = os.path.join(BASEDIR, 'static')

EXTERNAL_CSS = ['static/ExampleApp/css/style.css']
EXTERNAL_JS = []

def get_readme():
    path = os.path.join(BASEDIR, 'Readme.md')
    return cat(path)