import dash_core_components as dcc
import dash_html_components as html

from packages.utils import read_file_as_str
# from settings import info_page_file

# markdown_string = read_file_as_str(info_page_file)

markdown_string = '''
# This is Markdown
'''

layout = html.Div(className='container cm-top', children=[
    html.Div(className='row', children=[
        html.Div(className='col-md-10', children=[
            dcc.Markdown(markdown_string)
        ])
    ])])