from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import numpy as np

app = Dash(__name__)


app.layout = html.Div([
    dcc.Markdown('# Differential Equation:'),
    html.Div([
        'Plotting differential equations of the form dx/dt = λx',
        html.Div(id='diffeq'),
    ]),
    dcc.Graph(id='graph'),
    html.Div([
        dcc.Markdown('λ:', mathjax=True),
        dcc.Slider(-10, 10, step = 0.1, value = 1, marks={i: str(i) for i in range(-10, 11)}, id='lambda-slider', tooltip={'placement':'bottom'}),
    ]),
    html.Div([
        dcc.Markdown('$y_{0}$:', mathjax=True),
        dcc.Slider(-10, 10, step = 0.1, value = 1, marks={i: str(i) for i in range(-10, 11)}, id='ivp-slider', tooltip={'placement':'bottom'}),
    ]),
])


@callback(
    Output('graph', 'figure'),
    Input('lambda-slider', 'value'),
    Input('ivp-slider', 'value')
)
def update_graph(lam, x0):
    x = np.arange(-10, 10, 0.01)
    y = x0 * np.exp(lam * x)
    fig = px.line(x=x, y=y)
    fig.update_xaxes(range=[-10, 10])
    
    return fig

@callback(
    Output('diffeq', 'children'),
    Input('lambda-slider', 'value'),
)
def update_diffeq(lam):
    return f'dx/dt = {lam}x'

if __name__ == '__main__':
    app.run(debug=True)
