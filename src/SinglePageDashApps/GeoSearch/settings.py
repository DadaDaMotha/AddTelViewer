import os
from .utils.io import cat

BASEDIR = os.path.dirname(os.path.abspath(__file__))
APP_NAME = os.path.split(BASEDIR)[-1]

TEMPLATE_DIR = os.path.join(BASEDIR, 'templates')
REACT_WRAPPER = os.path.join(TEMPLATE_DIR, 'main_wrapper.html')
STATIC_FOLDER = os.path.join(BASEDIR, 'static')

EXTERNAL_CSS = []
EXTERNAL_JS = []

map_box_token = 'pk.eyJ1IjoiZGFkYWRhbW90aGEiLCJhIjoiY2ptZ2Y2bmlhMDJ4OTN2cWp2MW5pNmlxMCJ9.--w_TfMoej4yvld_tN919Q'


def get_readme():
    path = os.path.join(BASEDIR, 'Readme.md')
    return cat(path)