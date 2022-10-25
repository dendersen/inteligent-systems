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

#Funktion for x,y-værdier
def plot2 (Type1:List[Point],Type2: List[Point]) -> None:
  #Combine values for x and y
  x = (*(i.x for i in Type1),*( i.x for i in Type2))
  y = (*(i.y for i in Type1),*( i.y for i in Type2))
  #----------------
  #Plot size limit
  plt.xlim(min(x)-2, max(x)+2)
  plt.ylim(min(y)-2, max(y)+2)
  plt.grid()
  #----------------
  #Defines plot style
  plt.style.use("seaborn-whitegrid")
  #----------------
  #Makes point plot
  plt.plot([*(i.x for i in Type1)], [*(i.y for i in Type1)], "x", markeredgecolor="red")
  plt.plot([*(i.x for i in Type2)], [*(i.y for i in Type2)], "o", markeredgecolor="black", markerfacecolor="green")
  #printer et plot over hvor de to typer er
  plt.show()


def plot1 (type1:List[Point],showCordinate:bool = False, titel:str = 'Presition ud fra given k værdi (k-værdi angivet over punkt)', xlabel:str='K værdi', ylabel:str = 'Afvigelse fra facit (antal fejl)') -> None:
  x = [*(i.x for i in type1)]
  y = [*(i.y for i in type1)]
  #----------------
  #Plot visiuals
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(titel)
  #----------------
  #Plot size limit
  plt.xlim(min(x)-3, max(x)+3)
  plt.ylim(min(y)-3, max(y)+3)
  plt.grid()
  #----------------
  #Makes lines between each k-point
  plt.plot(x,y, "o--", linewidth=5, color="blue", markerfacecolor="pink")
  #Viser k-værdi for punkt
  for x,y in zip([*(i.x for i in type1)],[*(i.y for i in type1)]):
    if showCordinate:
      label = "{:.2f}".format(y)
    else:
      label = "{:.2f}".format(x)
    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,8),ha='center')
  #printer et plot over hvordan ændringer i k påvirker antal korrekte svar
  plt.show()

def plot_line():
  x_plot = arange(0.05,25,0.0001)   # start,stop,step
  y_plot = (0.2*(x_plot**2))+((x_plot**-1.6))-0.3
  return plt.plot(x_plot,y_plot)

def plotn(types:List[Point],animate:bool=False, line:bool=False,kvalue:str = 'k-værdi er ikke angivet')->None:
  if line:
    plot_line()

  print("\n\nbegin plot")
  if not animate:
    points = pointSorter(types)
    for i in points:
      x = [*(j.x for j in i)]
      y = [*(j.y for j in i)]
      plt.scatter(x,y,color = i[0].features[0])
  else:
    for j,l in zip(types,count()):
      # print("type j.x =",type(j.x))
      # print("type j.y =",type(j.y))
      # print("type j.features =",type(j.features[0]))
      try:
        plt.scatter(float(j.x),float(j.y),color = j.features[0])
      except:
        plt.scatter(float(j.x),float(j.y),color = colors[int(j.features[0])])
      label = ""
      try:
        label = j.features[1]
        plt.annotate(label,(j.x,j.y),textcoords="offset points",xytext=(0,8),ha='center')
      except:
        plt.annotate(label,(j.x,j.y),textcoords="offset points",xytext=(0,8),ha='center')
      if(l%40==0):
        plt.pause(1e-10)
  #labels
  plt.xlabel("x-value")
  plt.ylabel("y-value")
  plt.title(kvalue)
  #----------------
  #printer plot
  print("\nend plot")
  plt.show()

def plot3D(points:List[Point],labelx:str = "k-værdier", labely:str = "Afstandsfunktion nr.", labelz:str = "Antal forkerte svar")->None:
  try:
    Points:List[List[Point]] = pointSorter(points)
    
    ax = plt.axes(projection='3d')
    
    ax.set_xlabel(labelx)
    ax.set_ylabel(labely)
    ax.set_zlabel(labelz)
    ax.grid()
    a = ["square","circle"]
    b = []
    for i in Points:
      x_1 = [*(j.x for j in i)]
      y_1 = [*(j.y for j in i)]
      z_1 = [*(j.z for j in i)]
      markersize = [j.erga/100 for j in i]
      markercolor = [j.olga for j in i] 
      markershape = a[floor(i[0].features[0])]
      try:
        b.append(go.Scatter3d(x=x_1,
                            y=y_1,
                            z=z_1,
                            marker=dict(size=markersize,
                                        color=markercolor,
                                        symbol=markershape,
                                        opacity=0.9,
                                        reversescale=True,
                                        colorscale=colors2[0]),
                            line=dict (width=0.02),
                            mode='markers'))
      except:
        b.append(go.Scatter3d(x=x_1,
                            y=y_1,
                            z=z_1,
                            marker=dict(size=markersize,
                                        color=markercolor,
                                        symbol=markershape,
                                        opacity=0.9,
                                        reversescale=True,
                                        colorscale=colors2[0]),
                            line=dict (width=0.02),
                            mode='markers'))
    #Make Plot.ly Layout
    mylayout = go.Layout(title=dict(text="Colors shows range of, CO2 in ppm, and figure-type if occupied (square) or not (circle)"),
                        scene=dict(xaxis=dict(title="Temperature in Celcius"),
                                    yaxis=dict(title="Relative humidity in %"),
                                    zaxis=dict(title="Light in lux")),)
    #Plot and save html
    plotly.offline.plot({"data": b,
                        "layout": mylayout},
                        auto_open=True,
                        )
  except:
    ax = plt.axes(projection='3d')
    #point data
    x = [*(i.x for i in points)]
    y = [*(i.y for i in points)]
    z = [*(i.z for i in points)]
    
    ax.set_xlabel('k-værdier')
    ax.set_ylabel('Afstandsfunktion nr.')
    ax.set_zlabel('Antal forkerte svar')
    ax.grid()
    
    ax.scatter3D(x,y,z)
    plt.show()

def pointSorter(points:List[Point]) -> List[List[Point]]:
  sorted:List[List[Point]] = []
  for point in points:
    for i in sorted:
      if(i[0].features[0] == point.features[0]):
        i.append(point)
        break
    else:
      sorted.append([point])
  return sorted
