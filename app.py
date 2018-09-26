import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
from scipy import stats
from dash.dependencies import Input, Output

app = dash.Dash()
x = np.linspace(-20, 20, 1000)
xr = np.linspace(0, 20, 1000)
# pdf = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
# cdf = (1 + scipy.special.erf((x - mu) / np.sqrt(2 * sigma ** 2))) / 2


trace0 = go.Scatter(
    x=x,
    mode='lines',
    name='pdf',
    fill="tozerox",
    line=dict(color='#835AF8', width=3)
)

trace1 = go.Scatter(
    x=x,
    mode='lines',
    name='cdf',
    fill="tozeroy",
    line=dict(color='#7FA6EE', width=3)
)

trace2 = go.Scatter(
    x=xr,
    mode='lines',
    name='pdf',
    fill="tozerox",
    line=dict(color='#835AF8', width=3)
)

trace3 = go.Scatter(
    x=xr,
    mode='lines',
    name='cdf',
    fill="tozeroy",
    line=dict(color='#7FA6EE', width=3)
)

app.layout = html.Div(children=[
    html.H2(children='Analysis App'),

    html.Div([
        html.Div(dcc.Graph(animate=True, id='normal'), className="six columns"),
        html.Div(dcc.Graph(animate=True, id='rayleigh'), className="six columns")
    ], className="row"),

    html.Div([html.Label("Deviation \u03C3"),
              dcc.Slider(
                  id="sigma",
                  min=0,
                  max=5,
                  value=1,
                  step=0.1,
                  marks={i: str(i) for i in range(0, 6)}
              )], style={'padding': '10px'}),

    html.Div([html.Label("Mean \u03BC"),
              dcc.Slider(
                  id="mean",
                  min=-10,
                  max=10,
                  value=0,
                  step=None,
                  marks={i: str(i) for i in range(-10, 11, 2)}
              )], style={'padding': '10px'}),
], className='container', style={'height': 'auto'})


@app.callback(
    Output('normal', 'figure'),
    [Input('sigma', 'value'),
     Input('mean', 'value')])
def update_figure_1(sigma, mean):
    trace0['y'] = stats.norm.pdf(x, mean, sigma)
    trace1['y'] = stats.norm.cdf(x, mean, sigma)
    return {
        'data': [trace0, trace1],
        'layout': {
            'title': 'Normal distribution'
        }
    }


@app.callback(
    Output('rayleigh', 'figure'),
    [Input('sigma', 'value')])
def update_figure_2(sigma):  # scale parameter
    trace2['y'] = stats.rayleigh.pdf(xr, 0, sigma)
    trace3['y'] = stats.rayleigh.cdf(xr, 0, sigma)
    return {
        'data': [trace2, trace3],
        'layout': {
            'title': 'Rayleigh distribution'
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
