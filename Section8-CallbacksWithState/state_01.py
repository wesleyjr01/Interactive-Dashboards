import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='number-in',
              value=1,
              style={'fontSize': 25}),
    html.Button(id='submit-button',
                n_clicks=0,
                children='Submit Here',
                style={'fontSize': 24}),
    html.H1(id='number-out')
])


@app.callback(Output(component_id='number-out', component_property='children'),
              [Input(component_id='submit-button', component_property='n_clicks')],
              [State(component_id='number-in', component_property='value')])
def output(n_clicks, number):
    return "{} was typed in, button was clicked {} times".format(number, n_clicks)


if __name__ == '__main__':
    app.run_server()
