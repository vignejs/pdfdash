import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
from scipy import stats
from dash.dependencies import Input, Output

external_stylesheets = [
    # Normalize the CSS
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
    # Fonts
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto"
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.scripts.config.serve_locally = True

x = np.linspace(-20, 20, 1000)

xr = np.linspace(0, 20, 1000)

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

app.layout = html.Div([
    # Banner display
    html.Div([
        html.H2(
            'Probablity Distribution Functions',
            id='title'
        ),
        html.Img(
            src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe-inverted.png"
        )
    ], className="banner"),
    html.Div([
        html.Div([dcc.Graph(animate=True, id='normal'),
                  html.Div([html.Label("Deviation \u03C3"),
                            dcc.Slider(
                                id="sigma",
                                min=0,
                                max=5,
                                value=1,
                                step=0.1,
                                marks={i: str(i) for i in range(0, 6)}
                            )], style={'height': '60px'}),
                  html.Div([html.Label("Mean \u03BC"),
                            dcc.Slider(
                                id="mean",
                                min=-10,
                                max=10,
                                value=0,
                                step=None,
                                marks={i: str(i) for i in range(-10, 11, 2)})
                            ], style={'height': '60px'})
                  ], className="six columns"),
        html.Div([dcc.Graph(animate=True, id='rayleigh'),
                  html.Div([html.Label("Scale factor \u03C3"),
                            dcc.Slider(
                                id="scale",
                                min=0,
                                max=5,
                                value=1,
                                step=0.1,
                                marks={i: str(i) for i in range(0, 6)})
                            ], style={'height': '60px'}),
                  html.Label(id="rayleigh_mean"
                             ),
                  html.Label(id="rayleigh_skew",
                             children=[
                                 "Skewness: {:.4f}".format(stats.rayleigh.stats(moments='s'))
                             ]),
                  html.Label(id="rayleigh_kurtosis",
                             children=[
                                 "Kurtosis: {:.4f}".format(stats.rayleigh.stats(moments='k'))
                             ])
                  ], className="six columns")
    ])

], className='container')


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
    [Input('scale', 'value')])
def update_figure_2(scale):  # scale parameter
    trace2['y'] = stats.rayleigh.pdf(xr, 0, scale)
    trace3['y'] = stats.rayleigh.cdf(xr, 0, scale)
    return {
        'data': [trace2, trace3],
        'layout': {
            'title': 'Rayleigh distribution'
        }
    }


@app.callback(
    Output('rayleigh_mean', 'children'),
    [Input('scale', 'value')]
)
def rayliegh_mean(scale):
    mean = stats.rayleigh.mean(scale=scale)
    return "Mean: {:.4f}".format(mean)


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
