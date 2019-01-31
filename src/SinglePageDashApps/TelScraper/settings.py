import os
from .utils.io import cat

BASEDIR = os.path.dirname(os.path.abspath(__file__))
APP_NAME = os.path.split(BASEDIR)[-1]

TEMPLATE_DIR = os.path.join(BASEDIR, 'templates')
REACT_WRAPPER = os.path.join(TEMPLATE_DIR, 'main_wrapper.html')
STATIC_FOLDER = os.path.join(BASEDIR, 'static')

EXTERNAL_CSS = ['https://getbootstrap.com/docs/4.1/examples/dashboard/dashboard.css',
                'static/TelScraper/css/main.css',
                'static/TelScraper/css/load_ctrl_clr.css',
                ]
EXTERNAL_JS = ['https://unpkg.com/feather-icons/dist/feather.min.js']

dashbord_simple_script = """<script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script>
    <script>
      feather.replace()
    </script>
    """

def get_readme():
    path = os.path.join(BASEDIR, 'Readme.md')
    return cat(path)