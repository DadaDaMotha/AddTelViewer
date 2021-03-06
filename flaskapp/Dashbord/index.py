from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dte

from Dashbord.app import app
from Dashbord.pages import map_start, telscraper, info


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', className='mt'),
    html.Div(style={"display": "none"}, children=dte.DataTable(id="hidden")),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return map_start.layout
    if pathname == '/telscraper/':
        return telscraper.layout
    if pathname == '/info/':
        return info.layout
    else:
        return '404'


