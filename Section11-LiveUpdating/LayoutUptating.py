import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()


app.layout = html.Div([
    html.H1(id='live-update-text'),
    dcc.Interval(id='interval-component',
                 interval=2000,
                 n_intervals=0
                 )
])


@app.callback(Output(component_id='live-update-text', component_property='children'),
              [Input(component_id='interval-component', component_property='n_intervals')])
def update_layout(n):
    return "Crash free for {} refreshes".format(n)


if __name__ == '__main__':
    app.run_server()
