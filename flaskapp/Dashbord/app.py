from DashCustom.custom_class import DashResponsive
from server import server

app = DashResponsive(name="dashboard", sharing=True, server=server, url_base_pathname='/')
app.config.supress_callback_exceptions = True

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

# for script in external_scripts:
#     app.scripts.append_script({"external_url": script})

# Use this if there is no internet connection

# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True

# @app.server.route('/static/<path:path>')
# def static_file(path):
#     static_folder = os.path.join(basedir, 'static')
#     return send_from_directory(static_folder, path)


