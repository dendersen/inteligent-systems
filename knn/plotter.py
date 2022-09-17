import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

#Funktion for x,y-værdier
def plot (Type1:List[Tuple[int]],Type2: List[Tuple[int]]) -> None:
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

  x = np.concatenate((Type1[0],Type2[0]))
  y = np.concatenate((Type1[1],Type2[1]))
  #----------------
  #Plot size limit
  plt.xlim(min(x-2), max(x+2))
  plt.ylim(min(y-2), max(y+2))
  plt.grid()
  #----------------
  #Defines plot style
  plt.style.use("seaborn-whitegrid")
  #----------------
  #Makes point plot
  cross = plt.plot(Type1[0], Type1[1], "x", markersize=(100/(max(x)-min(y))), markeredgecolor="red")
  circle = plt.plot(Type2[0], Type2[1], "o", markersize=(100/(max(x)-min(y))), markeredgecolor="black", markerfacecolor="green")
  #printer et plot over hvor de to typer er
  plt.show()


def plotK (type1:List[List[int]]) -> None:
  #type1[0] giver liste over x
  type1[0]
  #type1[1] giver liste over y
  type1[1]
  #----------------
  #Plot size limit
  plt.xlim(min(type1[0]-2), max(type1[0]+2))
  plt.ylim(min(type1[1]-2), max(type1[1]+2))
  plt.grid()
  #----------------
  #Makes lines between each k-point
  plt.plot(type1[0], type1[1], "o--", linewidth=5, markersize=12, color="blue", markerfacecolor="pink")
  #printer et plot over hvordan ændringer i k pævirker antal korekte
  plt.show()