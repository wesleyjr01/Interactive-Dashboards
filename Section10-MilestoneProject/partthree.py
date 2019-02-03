import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol'),
    dcc.Input(id='my_stock_picker',
              value='TSLA'
              ),
    dcc.Graph(id='my_graph',
              figure={'data': [
                  {'x': [1, 2], 'y':[3, 1]}
              ], 'layout':{'title': 'Default Title'}}
              )
])


@app.callback(Output(component_id='my_graph', component_property='figure'),
              [Input(component_id='my_stock_picker', component_property='value')])
def update_graph(stock_ticker):
  start = datetime(2017, 1, 1)
  end = datetime(2017, 12, 31)
  df = web.DataReader(stock_ticker, 'iex', start, end)
  fig = {
      'data': [{'x': df.index, 'y': df.close}],
      'layout': {'title': stock_ticker}
  }
  return fig


if __name__ == '__main__':
  app.run_server()
