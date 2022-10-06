from itertools import count
from re import X
import matplotlib.pyplot as plt
from typing import List
from numpy import arange
from plotingTools.point import Point
import sys
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
  #printer et plot over hvordan ændringer i k pævirker antal korekte
  plt.show()

def plot_line():
  x_plot = arange(0.05,25,0.0001)   # start,stop,step
  y_plot = (0.2*(x_plot**2))+((x_plot**-1.6))-0.3
  return plt.plot(x_plot,y_plot)

def plotn(types:List[Point],line:bool=False,kvalue:str = 'k-værdi er ikke angivet')->None:
  for j,l in zip(types,count()):
    plt.scatter(j.x,j.y, color = j.features[0])
    label = ""
    try:
      label = j.features[1]
      plt.annotate(label,(j.x,j.y),textcoords="offset points",xytext=(0,8),ha='center')
    except:
      plt.annotate(label,(j.x,j.y),textcoords="offset points",xytext=(0,8),ha='center')
    if(l%4==0):
      plt.pause(1e-10)
  if line:
    plot_line()
  #labels
  plt.xlabel("x-value")
  plt.ylabel("y-value")
  plt.title(kvalue)
  #----------------
  #printer plot
  plt.show()

def plot3D(points:List[Point])->None:
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
  pass