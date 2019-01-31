from dash.dependencies import Input, Output, State

# Wrap everything into a function

def register(app):

    @app.callback(Output('output-1', 'children'), [Input('input', 'value')])
    def update_outout(value):
        return 'You have selected {}'.format(value)


    @app.callback(Output('output-2', 'children'), [Input('input', 'value')])
    def update_outout(value):
        return 'You have selected {}'.format(value)



    # ------------------------------------------------------------------------

    return app