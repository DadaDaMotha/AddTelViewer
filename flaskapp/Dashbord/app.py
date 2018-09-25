import os
from flask import send_from_directory
from DashCustom import layouts, custom_class
from server import server
import config
# app = dash.Dash(__name__, server=server, url_base_pathname='/dash')

app = custom_class.DashResponsive(name="dashbord", sharing=True, server=server, url_base_pathname='/')
app.inject_custom_css_before(layouts.bootstrap_css + layouts.dashbord_simple_css)
app.inject_custom_scripts_body(layouts.bootstrap_scripts + layouts.dashbord_simple_script)

# test_wrapper = """<div id="test-wrapper">(DashEntry)</div>"""
# app.set_main_wrapper(test_wrapper, replace_string='(DashEntry)')

wrapper = layouts.dashbord_simple
app.set_main_wrapper(wrapper, replace_string=layouts.repl_string)
# server = app.server
# # cache = Cache(server, config={
# #     'CACHE_TYPE': 'filesystem',
# #     'CACHE_DIR': 'cache-directory'
# # })
app.config.supress_callback_exceptions = True


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
#     app.scripts.append_script({"external_url": script})

# app.css.append_css({
#     'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })
# Use this if there is no internet connection

# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True


# @app.server.route('/static/<path:path>')
# def static_file(path):
#     static_folder = os.path.join(basedir, 'static')
#     return send_from_directory(static_folder, path)


