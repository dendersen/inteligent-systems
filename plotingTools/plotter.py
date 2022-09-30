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
  plt.xlim(min(x)-2, max(x)+2)
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


def plot1 (type1:List[Point]) -> None:
  x = [*(i.x for i in type1)]
  y = [*(i.y for i in type1)]
  #----------------
  #Plot size limit
  # plt.xlim(min(x)-2, max(x)+2)
  # plt.ylim(min(y)-2, max(y)+2)
  # plt.grid()
  #----------------
  #Makes lines between each k-point
  plt.plot([*(i.x for i in type1)],[*(i.y for i in type1)], "o--", linewidth=5, markersize=(100/(max(x)-min(y))), color="blue", markerfacecolor="pink")
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