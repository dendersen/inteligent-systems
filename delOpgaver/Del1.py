from plotingTools.point import Point
from plotingTools.plotter import plot2
from knn.testKNN import dataKnown1,dataKnown2,dataStart
from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

#1. Lav en class Point, der repræsenterer et punkt som initialiseres et tilfældigt sted på skærmen 
# og som har en label i form af en farve (rød/blå eller kat/hund…). Dette udgør mængden

#2. Lav en liste af disse Point punkter og visualiser dem på skærmen med forskellige farver
#Funktion for x,y-værdier
def plot2_randomcollor (Type1:List[Point],Type2: List[Point]) -> None:
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
  #Makes differebt collors
  colors = cm.rainbow(np.linespace(0, 1, len(y)))
  #Makes point plot
  for i, c in zip(y, colors):
    plt.scatter(x, y, color=c)  #printer et plot over hvor de to typer er
  plt.show()