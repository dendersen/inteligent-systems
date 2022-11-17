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

def Plot2D(points:List[Point],labelx:str = "x", labely:str = "y")->None:
  app = Dash(__name__)
  
  df = pd.read_csv('C:\DDU2\Plot tester\Data.csv')
  
  available_plots = df['PlotNr'].unique()
  
  app.layout = html.Div([
      dcc.Graph(
          id='clientside-graph-px'
      ),
      dcc.Store(
          id='clientside-figure-store-px'
      ),
      'Plot-version',
      dcc.Dropdown(available_plots, 'plot1', id='clientside-graph-PlotNr-px'),
      html.Hr(),
      html.Details([
          html.Summary('Contents of figure storage'),
          dcc.Markdown(
              id='clientside-figure-json-px'
          )
      ])
  ])
  
  @app.callback(
      Output('clientside-figure-store-px', 'data'),
      Input('clientside-graph-PlotNr-px', 'value')
  )
  def update_store_data(PlotNr):
      dff = df[df['PlotNr'] == PlotNr]
      return px.scatter(dff, x='x', y="y",symbol="Symbol")
  
  app.clientside_callback(
      """
      function(figure, scale) {
          if(figure === undefined) {
              return {'data': [], 'layout': {}};
          }
          const fig = Object.assign({}, figure, {
              'layout': {
                  ...figure.layout,
                  'yaxis': {
                      ...figure.layout.yaxis, type: scale
                  }
                }
          });
          return fig;
      }
      """,
      Output('clientside-graph-px', 'figure'),
      Input('clientside-figure-store-px', 'data')
  )
  
  @app.callback(
      Output('clientside-figure-json-px', 'children'),
      Input('clientside-figure-store-px', 'data')
  )
  def generated_px_figure_json(data):
      return '```\n'+json.dumps(data, indent=2)+'\n```'
  
  if __name__ == '__main__':
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