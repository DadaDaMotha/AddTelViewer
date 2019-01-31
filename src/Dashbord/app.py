from DashCustom import cdn, DashResponsive
from server import flask_server

app = DashResponsive(name="dashbord", sharing=True, server=flask_server, url_base_pathname='/')




# '/static/dash-technical-charting.css'

external_css = ['/static/custom_css.css',
                '/static/load_ctrl_clr.css'

]
for css in external_css:
    app.css.append_css({"external_url": css})
#
# external_scripts = ['https://code.jquery.com/jquery-3.3.1.slim.min.js',
#                     'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js',
#                     'https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js'
# ]
#
#
# for script in external_scripts:
#     app.scripts.append_script({"externalapp.config.supress_callback_exceptions = True_url": script})

# app.css.append_css({
#     'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })
# Use this if there is no internet connection


# @app.server.route('/static/<path:path>')
# def static_file(path):
#     static_folder = os.path.join(basedir, 'static')
#     return send_from_directory(static_folder, path)


