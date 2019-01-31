import dash
from . import cdn

class DashResponsive(dash.Dash):
    '''
    This class extends the dash.Dash class with a wrapper html element and other injections defined below
    '''
    def __init__(self, *args, **kwargs):

        super(DashResponsive, self).__init__(*args, **kwargs)

        self.wrapper_path = None
        self.static_page_title = 'DashResponsive'

        self.__cdn_css = """"""
        self.__cdn_js = """"""

    def add_external_css(self, list):
        """
        :param list: e.g ['/static/css/mycss.css']
        :return:
        """
        for css in list:
            self.css.append_css({"external_url": css})

    def add_external_js(self, list):
        """
        :param list: e.g ['/static/js/myscript.js']
        :return:
        """
        for js in list:
            self.scripts.append_script({"external_url": js})

    def cat(self, filepath):
        with open(filepath) as f:
            res = f.read()
        return res

    def use_styling_framework(self, name):
        supported = ['bootstrap4']
        assert name in supported, 'Available frameworks: {}'.format(". ".join(supported))

        if name == "bootstrap4":
            self.__cdn_css = cdn.bootstrap_css
            self.__cdn_js = cdn.bootstrap_scripts



    def interpolate_index(self, **kwargs):
        # check if a custom wrapper was defined
        if self.wrapper_path:
            try:
                new_app_entry = self.cat(self.wrapper_path)
            except Exception as e:
                print('Template File %s could not be read' %self.wrapper_path)
                print(str(e))
                new_app_entry = kwargs.get('app_entry')
        else:
            new_app_entry = kwargs.get('app_entry')


        return '''
        <!DOCTYPE html>
        <html>
            <head>
                {metas}
                <title>{title}</title>
                {cdn_css}
                {css}
            </head>
            <body>
                {app_entry}
                {config}
                {scripts}
                {cdn_js}
            </body>
        </html>
        '''.format(
            metas=kwargs.get('metas'),
            title=self.static_page_title,
            cdn_css=self.__cdn_css,
            app_entry=new_app_entry,
            config=kwargs.get('config'),
            scripts=kwargs.get('scripts'),
            css=kwargs.get('css'),
            cdn_js=self.__cdn_js
        )

