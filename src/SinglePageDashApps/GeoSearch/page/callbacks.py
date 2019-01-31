from dash.dependencies import Input, Output, State
import numpy as np
from packages.GeoTools import GeoLocator
from .layout import PLZ
import plotly.graph_objs as go
from SinglePageDashApps.GeoSearch import settings



# Wrap everything into a function

def register(app):
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
                accesstoken=settings.map_box_token,
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


    # ------------------------------------------------------------------------

    return app