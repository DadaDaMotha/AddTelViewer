
from SinglePageDashApps.TelScraper.settings import get_readme

# to whatever you want here with functions etc and wrap all into one div that will be served as layout

import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dte
import datetime as dt


my_layout = html.Div(className='container cm-top', children=[

            html.H2('Search Local CH and TelSearch'),


            html.Div(className='row', children=[
                html.Div(className='col-sm-2', children=[
                    dcc.Dropdown(id='source-dropdown', className='mt',
                             options=[{'label': x, 'value': x} for x in ['TelSearch', 'LocalCH']], value='LocalCH',
                 clearable=False)
                ]),

                html.Div(className='col-sm-3', children=[
                    dcc.Input(id="was-query", className='form-control form-control mt', type="text", size=20,
                              placeholder="Was...")
                ]),
                html.Div(className='col-sm-3', children=[
                    dcc.Input(id="wo-query", className='form-control form-control mt', type="text", size=20,
                              placeholder="Wo...")
                ]),
                html.Div(className='col-sm-2', children=[
                dcc.Dropdown(id='cat-dropdown', className='mt',
                             options=[{'label': x, 'value': x} for x in ['Private', 'Firmen']], value='',
                 clearable=True, placeholder='Kategorie: Beide')
                ]),
                html.Div(className='col-sm-3', children=[
                    html.Button(id="button-query", className='btn btn-outline-info btn-primary mt', children="SUCHEN",
                                n_clicks=0),
                ]),
            ]),
            html.Div(className='row', children=[
                html.Div(className='col-sm-12', children=[

                    html.Div(className='mt', children=[
                        dte.DataTable(
                            rows=[{}],
                            # columns=sorted(df_tel_result.columns), # optional - sets the order of columns
                            row_selectable=False,
                            editable=False,
                            resizable=True,
                            filterable=True,
                            sortable=True,
                            selected_row_indices=[],
                            id='datatable-query'
                        )
                    ]),
                    html.Div(className='col-sm-3', children=[
                        html.A('DOWNLOAD',
                                id='download-link',
                                download="localch_{}.csv".format(dt.datetime.now().strftime('%Y_%m_%d_%H%M')),
                                href="",
                                target="_blank",
                                className='btn btn-info btn-primary mt'
                            ),
                    ])
                ])
            ])
        ])



#
# @app.callback(
#     Output('geopy-search', 'value'),
#     [Input('choose-plz', 'value')])
#
# def clear_search_field(plz):
#     return []






def render():
    print('Calling render layout')
    return my_layout

