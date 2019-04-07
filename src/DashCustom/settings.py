import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))


# used for the collectstatic script
DASH_APPS_PARENT_DIR = os.path.join(BASEDIR, 'SinglePageDashApps')
print(DASH_APPS_PARENT_DIR)
