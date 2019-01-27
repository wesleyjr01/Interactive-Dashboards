import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import json
import base64

app = dash.Dash()

df = pd.read_csv('wheels.csv')


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


app.layout = html.Div([
    html.Div(dcc.Graph(id='wheels-plot',
                       figure={'data': [go.Scatter(
                                        x=df['color'],
                                        y=df['wheels'],
                                        dy=1,
                                        mode='markers',
                                        marker={'size': 15})],
                               'layout': go.Layout(title='Test',
                                                   hovermode='closest')}
                       ), style={'width': '30%', 'float': 'left'}),
    html.Div([html.Img(id='hover-data', src='children', height=300)],
             style={'paddingTop': 35})
])


@app.callback(Output(component_id='hover-data', component_property='src'),
              [Input(component_id='wheels-plot', component_property='hoverData')])
# [Input(component_id='wheels-plot', component_property='clickData')])
def callback_image(hoverData):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = 'images/'
    return encode_image(path + df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()
