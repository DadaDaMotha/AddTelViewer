from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from Dashbord.app import app

from packages.GeoTools import GeoLocator
from packages.PLZTools import PLZLoader

map_center_lat = 46.61
map_center_long = 6.50

PLZ = PLZLoader(test_sample=False)
# df = pd.read_csv(
#     'https://raw.githubusercontent.com/plotly' +
#     '/datasets/master/2011_february_us_airport_traffic.csv')

# address = 'Zurich City'
#
# GL = GeoLocator()
# query = GL.make_query(address)
# query.info_print()
# center_lat, center_long = query.boundbox_center()
map_box_token = 'pk.eyJ1IjoiZGFkYWRhbW90aGEiLCJhIjoiY2ptZ2Y2bmlhMDJ4OTN2cWp2MW5pNmlxMCJ9.--w_TfMoej4yvld_tN919Q'

graph_layout = go.Layout(
    autosize=False,
    height=450,
    hovermode='closest',

    mapbox=dict(
        accesstoken=map_box_token,
        bearing=0,
        center=dict(
            lat=map_center_lat,
            lon=map_center_long
        ),
        pitch=0,
        zoom=0
    ),
)

layout = html.Div(className='container mt-4', children=[

    html.H2('Interactive Search with geopy and PLZ CH'),

    html.Div(className='row my-4', children=[
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


# layout = html.Div(className='container', children=[
#     html.Div(className='three columns', children=[
#             html.Div(id='lasso')], style={'display':'none'}),
#
#         html.Div(className='ten columns', children=[
#             html.H1('Interactive Search with geopy and PLZ CH'),
#             dcc.Dropdown(id='choose-plz', options=PLZ.get_Dash_PLZ_all_opts(loc_only=False), value=1270, multi=False),
#             dcc.Input(type="text", size=20, id="geopy-search", placeholder="Irgendwas suchen..."),
#             html.Button(id="button-search", children="SEARCH", n_clicks=0),
#
#             dcc.Graph(id='graph', figure=dict(data=[], layout=graph_layout))])
#
#         ])

# @app.callback(
#     Output('lasso', 'children'),
#     [Input('graph', 'selectedData')])
# def display_data(selectedData):
#     return json.dumps(selectedData, indent=2)

@app.callback(
    Output('graph', 'figure'),
    [Input('choose-plz', 'value'), Input('button-search', 'n_clicks')],
    state=[State('geopy-search', 'value')])
def display_data(plz_name, n_clicks, query):
    print(type(plz_name))
    print(plz_name)

    if n_clicks > 0 and query:
        global GL
        GL = GeoLocator()
        GL.store_query(query)
        lat = [GL.lat]
        lon = [GL.long]
        names = [GL.addr]
        if GL.location:
            zoom = 14
        else:
            zoom = 6.5

        # GL.info_print()
    else:
        lat, lon, names = PLZ.get_Dash_lat_lon_lists(plz_name)  # returns list of strings
        zoom = 10
    data = [
        go.Scattermapbox(
            lat=lat,
            lon=lon,
            mode='markers',
            marker=dict(
                size=14,
                symbol='star',
                color='orange'
            ),
            text=names,
            hoverinfo='text'
        )
    ]

    graph_layout = go.Layout(
        autosize=True,
        height=500,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),
        showlegend=False,
        legend=dict(
            bgcolor='#ddd'),
        hovermode='closest',
        mapbox=dict(
            # layers=[
            #     dict(
            #         sourcetype='geojson',
            #         source=r"D:\Python3_Scripts\bauer-connect\od_static_files\plz_verzeichnis_v2.geojson",
            #         type='fill',
            #         color='rgba(163,22,19,0.8)'
            #     )],
            style='light',
            accesstoken=map_box_token,
            bearing=0,
            center=dict(
                lat=np.float(lat[0]),
                lon=np.float(lon[0])
            ),
            pitch=0,
            zoom=zoom
        ),
    )

    fig = dict(data=data, layout=graph_layout)
    return fig


@app.callback(
    Output('geopy-search', 'value'),
    [Input('choose-plz', 'value')])
def clear_search_field(plz):
    return []
