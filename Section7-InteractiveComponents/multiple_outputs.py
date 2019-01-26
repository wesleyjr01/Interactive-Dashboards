import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('wheels.csv')

app = dash.Dash()

app.layout = html.Div([
    dcc.RadioItems(id='wheels-input',
                   options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
                   value=1
                   ),
    html.Div(id='wheels-output'),
    html.Hr(),  # Line Separator
    dcc.RadioItems(id='colors-input',
                   options=[{'label': i, 'value': i} for i in df['color'].unique()],
                   value='blue'),
    html.Div(id='colors-output')
], style={'fontFamily': 'helvetica', 'fontSize': 18})


@app.callback(Output(component_id='wheels-output', component_property='children'),
              [Input(component_id='wheels-input', component_property='value')])
def callback_a(wheels_value):
    return "You chose {}".format(wheels_value)


@app.callback(Output(component_id='colors-output', component_property='children'),
              [Input(component_id='colors-input', component_property='value')])
def callback_b(colors_value):
    return "You chose {}".format(colors_value)


if __name__ == '__main__':
    app.run_server()
