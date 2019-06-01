import flask
from flask import send_from_directory
import os
import config

basedir = os.path.dirname(os.path.abspath(__file__))
application = flask.Flask(__name__)
application.config.from_object(config.DevelopmentConfig)

@application.route('/hello')
def hello():
    return 'Hello, World!'


if not os.path.isfile(os.path.join(basedir, 'static', 'custom_css.css')):
    raise AssertionError('CSS Files custom not found in path {}'.format(os.path.join(basedir, 'static')))
# For production, use a nginx to application static files
@application.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(basedir, 'static')
    return send_from_directory(static_folder, path)
