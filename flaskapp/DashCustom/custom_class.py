import dash
class DashResponsive(dash.Dash):
    '''
    This class extends the dash.Dash class with a wrapper html element and other injections defined below
    '''
    def __init__(self, *args, **kwargs):

        super(DashResponsive, self).__init__(*args, **kwargs)


        self.main_wrapper = ""
        self.replace_string = ""

        self.custom_css_before = ""
        self.custom_css_after = ""

        self.custom_scripts_body = ""
        self.custom_scripts_footer_before = ""
        self.custom_scripts_footer_after = ""

        self.inject_before_entrypoint = ""
        self.inject_after_entrypoint = ""

        self.inject_footer = ""
        self.static_page_title = 'DashResponsive'



    def inject_html_before(self, raw_html):
        self.inject_before_entrypoint = raw_html

    def inject_html_after(self, raw_html):
        self.inject_after_entrypoint = raw_html

    def inject_html_footer(self, raw_html):
        self.inject_footer = raw_html

    def inject_custom_css_before(self, raw_html):
        self.custom_css_before = raw_html

    def inject_custom_css_after(self, raw_html):
        self.custom_css_after = raw_html

    def inject_custom_scripts_body(self, raw_html):
        self.custom_scripts_body = raw_html

    def inject_custom_sripts_footer_after(self, raw_html):
        self.custom_scripts_footer_after = raw_html

    def inject_custom_sripts_footer_before(self, raw_html):
        self.custom_scripts_footer_before = raw_html

    def set_main_wrapper(self, raw_html, replace_string):
        self.replace_string = replace_string
        self.main_wrapper = raw_html

    def dash_div(self):
        return ("""
        <div id="react-entry-point">
                    <div class="_dash-loading">
                        Loading...
                    </div>
        </div>
        """)

    def create_wrapper(self):

        dash_cont = """
        <div id="react-entry-point">
                    <div class="_dash-loading">
                        Loading...
                    </div>
        </div>
        """
        return self.main_wrapper.replace(self.replace_string, dash_cont)

    # Overriding from https://github.com/plotly/dash/blob/master/dash/dash.py#L282
    def index(self, *args, **kwargs):
        scripts = self._generate_scripts_html()
        css = self._generate_css_dist_html()
        config = self._generate_config_html()
        # title = getattr(self, 'title', 'Dash')
        title = self.static_page_title
        return (f'''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
                <meta name="description" content="">
                <meta name="author" content="">
                <title>{title}</title>
                {self.custom_css_before}
                {css}
                {self.custom_css_after}
            </head>
            <body>
                {self.inject_before_entrypoint}
                {self.create_wrapper()}
                {self.inject_after_entrypoint}
                {self.custom_scripts_body}
            </body>
            <footer>
                {config}
                {self.custom_scripts_footer_before}
                {scripts}
                {self.custom_scripts_footer_after}
            </footer>
        </html>
        ''')
