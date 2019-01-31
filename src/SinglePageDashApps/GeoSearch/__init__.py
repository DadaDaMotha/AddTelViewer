from .page import callbacks, layout
from .utils.io import cat
from . import settings
from DashCustom import DashResponsive


def create_app(server=None,
               page_title='CustomDash',
               styling_framework=None,
               **kwargs):
    assert server, 'Please specify a server for this Dash app!'
    assert page_title, 'Please specify a page title for your app (head section)'
    app = DashResponsive(name=settings.APP_NAME, server=server, styling_framework=styling_framework, **kwargs)
    app.static_page_title = page_title
    app.wrapper_path = settings.REACT_WRAPPER
    app.layout = layout.render
    app = callbacks.register(app)
    app.config.supress_callback_exceptions = False

    if styling_framework:
        app.use_styling_framework(styling_framework)

    if settings.EXTERNAL_CSS:
        app.add_external_css(settings.EXTERNAL_CSS)

    if settings.EXTERNAL_JS:
        app.add_external_js(settings.EXTERNAL_JS)

    return app







