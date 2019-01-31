import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from packages.PLZTools import PLZLoader
from SinglePageDashApps.GeoSearch import settings


map_center_lat = 46.61
map_center_long = 6.50

PLZ = PLZLoader(test_sample=False)


graph_layout = go.Layout(
    autosize=False,
    height = 450,
    hovermode='closest',

    mapbox=dict(
        accesstoken=settings.map_box_token,
        bearing=0,
        center=dict(
            lat=map_center_lat,
            lon=map_center_long
        ),
        pitch=0,
        zoom=0
    ),
)

my_layout = html.Div(className='container cm-top', children=[

            html.H2('Interactive Search with geopy and PLZ CH'),


            html.Div(className='row', children=[
                html.Div(className='col-sm-3', children=[

                        dcc.Dropdown(id='choose-plz', className='mt',
                                     options=PLZ.get_Dash_PLZ_all_opts(loc_only=False), value='1217!!Meyrin 1',
                                     multi=False)
                    ]),
                html.Div(className='col-sm-3', children=[
                    dcc.Input(id="geopy-search", className='form-control form-control mt', type="text", size=20,
                              placeholder="Irgendwas suchen...")
                ]),
                html.Div(className='col-sm-3', children=[
                    html.Button(id="button-search", className='btn btn-outline-info btn-primary mt', children="SUCHEN",
                                n_clicks=0),
                ]),
            ]),
            dcc.Graph(id='graph', className='shadow mt', figure=dict(data=[], layout=graph_layout))


        ])



def render():
    print('Calling render layout')
    return my_layout

