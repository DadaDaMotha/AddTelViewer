# DONT CHANGE THIS FILENAME OR SERVER NAME

from server import application
# This seems unused but is important

# from Dashbord import app as app1
import Dashbord.index

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
