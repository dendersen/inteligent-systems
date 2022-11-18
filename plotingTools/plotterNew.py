from itertools import count
from math import floor
from pyexpat import features
from re import X
import matplotlib.pyplot as plt
from typing import List
from numpy import arange
from plotingTools.point import Point
from plotingTools.colorList import colors
from plotingTools.colorList import colors2
import plotly
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import json

def Plot2D()->None:
  external_stylesheets = ['C:\DDU2\Plot tester\Layout.css']
  
  app = Dash(__name__, external_stylesheets=external_stylesheets)
  
  df = pd.read_csv('C:\DDU2\Plot tester\Data.csv')
  
  available_plots = df['PlotNr'].unique()
  
  app.layout = html.Div([
    html.P("Change figure width:"),
    dcc.Slider(id='slider', min=200, max=1900, step=25, value=1900,
              marks={x: str(x) for x in [100,300,500,700,900,1100,1300,1500,1700,1900]}),
    
    dcc.Graph(id='clientside-graph-px'),
    dcc.Store(
      id='clientside-figure-store-px'
    ),
    'Plot-version',
    dcc.Dropdown(available_plots, 'hello', id='clientside-graph-PlotNr-px'),
    html.Details([
      html.Summary('Contents of figure storage'),
      dcc.Markdown(
        id='clientside-figure-json-px'
      )
    ])
  ])
  
  @app.callback(
    Output('clientside-figure-store-px', 'data'),
    Input('clientside-graph-PlotNr-px', 'value'),
    Input('slider', 'value')
  )
  
  def update_store_data(PlotNr,width):
    dff = df[df['PlotNr'] == PlotNr]  
    dff["Color"] = dff["Color"].astype(str)
    fig = px.scatter(dff, x='x', y="y",color="Color",height=680)
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",)
    fig.update_layout(width=int(width))
    fig.update_traces(marker=dict(size=18,
                      line=dict(width=2,
                        color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    return fig
  
  app.clientside_callback(
    """
    function(figure, slider) {
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
              }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px', 'figure'),
    Input('clientside-figure-store-px', 'data'),
  )
  
  @app.callback(
    Output('clientside-figure-json-px', 'children'),
    Input('clientside-figure-store-px', 'data'),)
  
  def generated_px_figure_json(data):
    return '```\n'+json.dumps(data, indent=2)+'\n```'
  
  app.run_server(debug=True)

def plot6D(points:List[Point],labelx:str = "k-værdier", labely:str = "Afstandsfunktion nr.", labelz:str = "Antal forkerte svar")->None:
  Points:List[List[Point]]
  
  #Writes the cordinates of each point, this code automaticly makes different types om markershapes, markercollors and markersizes based on values.
  for i in Points:
    x_1 = [*(j.x for j in i)]
    y_1 = [*(j.y for j in i)]
    z_1 = [*(j.z for j in i)]
    markersize = [j.erga/100 for j in i]
    markercolor = [j.olga for j in i] 
    markershape = [j.features[0] for j in i]
    
    colorscales = px.colors.named_colorscales()
    app = Dash(__name__)
    
    app.layout = html.Div([
      html.H4('Interactive Plotly Express color scale selection'),
      html.P("Color"),
      dcc.Dropdown(
        id='dropdown',
        options=colorscales,
        value='viridis'
      ),
      dcc.Graph(id="graph"),
    ])
    
    @app.callback(
      Output("graph", "figure"),
      Input("dropdown", "value"))
    def change_colorscale(scale):
      df = pd.DataFrame({
        "x_1": x_1,
        "y_1": y_1,
        "z_1": z_1,
        "markercolor": markercolor,
        "markersize": markersize,
        "markershape": markershape
      })
      fig = px.scatter_3d(
        df, x="x_1", y="y_1", z="z_1",
        color="markercolor",color_continuous_scale=scale,
        size="markersize",
        symbol='markershape'
        )
      return fig
  
  app.run_server(debug=True)
