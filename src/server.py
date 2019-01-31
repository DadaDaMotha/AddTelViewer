import flask
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
import settings
from SinglePageDashApps import ExampleApp, TelScraper, GeoSearch

flask_server = flask.Flask(__name__)
flask_server.config.from_object(settings.Config)
# flask_server.static_folder = settings.STATIC_ROOT

db = SQLAlchemy(flask_server)

# For production, use a nginx to server static files
@flask_server.route('/static/<path:path>')
def static_file(path):
    return send_from_directory(settings.STATIC_ROOT, path)


dash1 = ExampleApp.create_app(server=flask_server,
                              url_base_pathname='/example/',
                              page_title='Example',
                              styling_framework='bootstrap4')

dash2 = TelScraper.create_app(server=flask_server,
                              url_base_pathname='/tel/',
                              page_title='TelScraper',
                              styling_framework='bootstrap4')

dash3 = GeoSearch.create_app(server=flask_server,
                              url_base_pathname='/map/',
                              page_title='GeoSearch',
                              styling_framework='bootstrap4')



@flask_server.route('/example')
def render_example():
    return flask.redirect('/example')


@flask_server.route('/tel')
def render_telscraper():
    return flask.redirect('/tel')

@flask_server.route('/')
def render_map():
    return flask.redirect('/map')



