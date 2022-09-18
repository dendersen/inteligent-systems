import matplotlib.pyplot as plt
from typing import List, Tuple

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
  plt.xlim(min(x)-2, max(x)+2)
  plt.ylim(min(y)-2, max(y)+2)
  plt.grid()
  #----------------
  #Makes lines between each k-point
  plt.plot(type1[0], type1[1], "o--", linewidth=5, markersize=(100/(max(x)-min(y))), color="blue", markerfacecolor="pink")
  #printer et plot over hvordan ændringer i k pævirker antal korekte
  plt.show()

def plotn(types:List[List[Point]])->None:
  
  colors = ["aqua","green","plum","grey","purple","salmon","black","khaki","sienna","blue","lavender","chartresue","lightgreen","teal","brown","lightblue","tan","chocolate","lime","tomato","coral","magenta","turquoise","crimson","maroon","violet","cyan","navy","wheat","darkblue","olive","darkgreen","orange","yellow","fuchsia","orangered","pink"]
  
  plt.xlim(max(j.x for i in types for j in i),min(j.x for i in types for j in i))
  plt.ylim(max(j.y for i in types for j in i), min(j.y for i in types for j in i))
  plt.grid()
  
  for i in types:
    plt.plot([*(j.x for j in types[i])],[*(j.y for j in types[i])],"o", marjersize =(100/(max(j.x for i in types for j in i)-min(j.y for i in types for j in i))),color = colors[i%len(colors)],markerfacecolor = colors[(i - i%len(colors))/len(colors) % len(colors)])
  
  plt.show()