import pandas as pd
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
# import dash_table_experiments as dte
import dash_table as dte
from Dashbord.app import app
from six.moves.urllib.parse import quote
import datetime as dt


from packages.tel_scraper import LocalCH, TelSearch

layout = html.Div(className='container mt-4', children=[

            html.H2('Search Local CH and TelSearch'),


            html.Div(className='row my-4', children=[
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
            ]),
                html.Div(className='row my-4', children=[
                html.Div(className='col-sm-3', children=[
                    html.Button(id="button-query", className='btn btn-outline-info btn-primary mt', children="SUCHEN",
                                n_clicks=0),
                ]),
            ]),
            html.Div(className='row my-4', children=[
                html.Div(id='table-div', className='col-sm-12', children=[

                    html.Div(className='mt', children=[
                        dte.DataTable(
                            id='datatable-query',
                            columns=[{}],
                            data=[{}],
                            style_table={'width': '100%'},
                            content_style='grow',
                            style_cell={'text-align':'left', 'padding-left': '1em'},
                            style_as_list_view=True

                        )
                    ]),
                    html.A('DOWNLOAD',
                            id='download-link',
                            download="localch_{}.csv".format(dt.datetime.now().strftime('%Y_%m_%d_%H%M')),
                            href="",
                            target="_blank",
                            className='btn btn-info btn-primary mt-4'
                        ),
                ])
            ])
        ])

@app.callback(
    [Output('datatable-query', 'columns'), Output('datatable-query', 'data')],
    [Input('button-query', 'n_clicks')],
    state=[State('was-query', 'value'), State('wo-query', 'value'),
           State('cat-dropdown', 'value'), State('source-dropdown', 'value')])
def get_data(n_clicks, was, wo, cat, source):

    if (n_clicks > 0) and (was or wo):

        print('type wo', type(wo))
        print('type was', type(was))
        print('type cat', type(cat))
        print('type cat', type(source))

        query_dict = {
            'was': was,
            'wo': wo,
            'category': cat
        }

        if source == 'LocalCH':
            df_query = LocalCH.page_aggregator(query_dict, max_pages=5)
            df_query = df_query[df_query.columns.difference(['Betriebsart'])]
        elif source == 'TelSearch':
            df_query = TelSearch.page_aggregator(query_dict, max_pages=5)
        else:
            return [{}]

        df = df_query[df_query.columns.difference(['URL', 'query'])]
        columns = [{'name': i, 'id': i} for i in df.columns]

        return columns, df.to_dict('records')
    else:
        # return [{'id':'column-1', 'name':'number'}, {'id':'column-2', 'name':'city'},
        #                              {'id':'column-3', 'name':'country'}],\
        #        [{'column-1': 4.5, 'column-2': 'montreal', 'column-3': 'canada'},
        #                           {'column-1': 8, 'column-2': 'boston', 'column-3': 'america'}]
        return [{}], [{}]

@app.callback(
    Output('download-link', 'href'),
    [Input('datatable-query', 'derived_viewport_data')])
def update_download_link(rows):
    if not rows == [{}]:
        dff = pd.DataFrame.from_dict(rows, 'columns')
        csv_string = dff.to_csv(index=False, encoding='utf-8', sep=';')
        csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + quote(csv_string)
        return csv_string
    return ""

#
# @app.callback(
#     Output('geopy-search', 'value'),
#     [Input('choose-plz', 'value')])
#
# def clear_search_field(plz):
#     return []
