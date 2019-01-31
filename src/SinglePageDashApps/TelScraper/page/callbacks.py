from dash.dependencies import Input, Output, State
from packages.tel_scraper import TelSearch, LocalCH
import pandas as pd
from six.moves.urllib.parse import quote    # TODO: check compatibiliy


# Wrap everything into a function

def register(app):

    @app.callback(
        Output('datatable-query', 'rows'),
        [Input('button-query', 'n_clicks')],
        state=[State('was-query', 'value'), State('wo-query', 'value'),
               State('cat-dropdown', 'value'), State('source-dropdown', 'value')])
    def fill_data(n_clicks, was, wo, cat, source):

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
            elif source == 'TelSearch':
                df_query = TelSearch.page_aggregator(query_dict, max_pages=5)
            else:
                return [{}]

            df_query_final = df_query[df_query.columns.difference(['URL', 'query'])]

            table_cont = df_query_final.to_dict('records')
            return table_cont
        else:
            return [{}]

    @app.callback(
        Output('download-link', 'href'),
        [Input('datatable-query', 'rows')])
    def update_download_link(rows):
        if not rows == [{}]:
            dff = pd.DataFrame.from_dict(rows, 'columns')
            csv_string = dff.to_csv(index=False, encoding='utf-8', sep=';')
            csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + quote(csv_string)
            return csv_string
        return ""

    # ------------------------------------------------------------------------

    return app