from dash import Dash, html, dcc, Input, Output, callback, dash_table
import pandas as pd
from collections import OrderedDict


app = Dash(__name__)

app.layout = html.Div([
    dcc.Tabs(id='tabs-test-1', value='tab-test-1', children=[
        dcc.Tab(label='Tab One', value='tab-test-1'),
        dcc.Tab(label='Tab Two', value='tab-test-2'),
    ]),
    html.Div(id='tabs-content-test')
])

@callback(Output('tabs-content-test', 'children'),
          Input('tabs-test-1', 'value'))
def render_content(tab):
    if tab == 'tab-test-1':
        return html.Div([
            html.H3('Tab content 1'),
            dcc.Graph(
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'tab-test-2':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs-dcc',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])



if __name__ == '__main__':
    app.run(debug=True)
