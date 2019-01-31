import dash_html_components as html
import dash_core_components as dcc

from SinglePageDashApps.ExampleApp.settings import get_readme

# to whatever you want here with functions etc and wrap all into one div that will be served as layout

my_layout = html.Div([
        dcc.Markdown(get_readme()),
        html.Div(id='output-1'),
        html.Div(id='output-2'),
        dcc.Dropdown(
            id='input', options=[{
                'label': i,
                'value': i
            } for i in ['a', 'b']])
    ])









def render():
    print('Calling render layout')
    return my_layout

