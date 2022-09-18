import matplotlib.pyplot as plt
from typing import List, Tuple

from plotingTools.point import Point

#Funktion for x,y-værdier
def plot2 (Type1:List[Point],Type2: List[Point]) -> None:
  #type1[0] giver liste over x af type 1
  # type1[0]
  #type1[1] giver liste over y af type 1
  # type1[1]
  #type2[0] giver liste over x af type 2
  # type2[0]
  #type2[1] giver liste over y af type 2
  # type2[1]
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
  cross = plt.plot([*(i.x for i in Type1)], [*(i.y for i in Type1)], "x", markersize=(100/(max(x)-min(y))), markeredgecolor="red")
  circle = plt.plot([*(i.x for i in Type2)], [*(i.y for i in Type2)], "o", markersize=(100/(max(x)-min(y))), markeredgecolor="black", markerfacecolor="green")
  #printer et plot over hvor de to typer er
  plt.show()


def plot1 (type1:List[Point]) -> None:
  #type1[0] giver liste over x
  type1[0]
  #type1[1] giver liste over y
  type1[1]
  #----------------
  #Plot size limit
  plt.xlim(0, max(type1[0])+2)
  plt.ylim(min(type1[1])-2, max(type1[1])+2)
  plt.grid()
  #----------------
  #Makes lines between each k-point
  plt.plot(type1[0], type1[1], "o--", linewidth=5, markersize=12, color="blue", markerfacecolor="pink")
  #printer et plot over hvordan ændringer i k pævirker antal korekte
  plt.show()