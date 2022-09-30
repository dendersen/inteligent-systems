from re import X
import matplotlib.pyplot as plt
from typing import List
from numpy import arange
from plotingTools.point import Point

#Funktion for x,y-værdier
def plot2 (Type1:List[Point],Type2: List[Point]) -> None:
  #type1[0] giver liste over x af type 1
  #type1[1] giver liste over y af type 1
  #type2[0] giver liste over x af type 2
  #type2[1] giver liste over y af type 2
  #----------------
  #Combine values for x and y
  x = (*(i.x for i in Type1),*( i.x for i in Type2))
  y = (*(i.y for i in Type1),*( i.y for i in Type2))
  #----------------
  #Plot size limit
  plt.xlim(min(x), max(x))
  plt.ylim(min(y)-2, max(y)+2)
  plt.grid()
  #----------------
  #Defines plot style
  plt.style.use("seaborn-whitegrid")
  #----------------
  #Makes point plot
  plt.plot([*(i.x for i in Type1)], [*(i.y for i in Type1)], "x", markersize=(100/(max(x)-min(y))), markeredgecolor="red")
  plt.plot([*(i.x for i in Type2)], [*(i.y for i in Type2)], "o", markersize=(100/(max(x)-min(y))), markeredgecolor="black", markerfacecolor="green")
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
  plt.plot(x,y, "o--", linewidth=5, markersize=((max(x)+max(y))/4), color="blue", markerfacecolor="pink")
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

def plotn(types:List[Point],line:bool=False)->None:
  for j in types:
    plt.scatter(j.x,j.y, color = j.features[0])
  if line:
    plot_line()
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