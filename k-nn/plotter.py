import matplotlib.pyplot as plt
import numpy as np
from typing import List
# #Points
# x_1 = [2,3]
# y_1 = [4,5]

# x_2 = [3,3]
# y_2 = [1,2]
# #Combine values for x and y
# x = np.concatenate((x_1,x_2))
# y = np.concatenate((y_1,y_2))
# #----------------
# #Plot size limit
# plt.xlim(min(x-2), max(x+2))
# plt.ylim(min(y-2), max(y+2))
# plt.grid()
# #----------------
# #Defines plot style
# plt.style.use("seaborn-whitegrid")
# #----------------
# #Makes the plot
# cross = plt.plot(x_1, y_1, "x", markersize=20, markeredgecolor="red")
# circle = plt.plot(x_2, y_2, "o", markersize=20, markeredgecolor="black", markerfacecolor="green")
# plt.show(cross,circle)

def plot (type1:List[List[int]],type2: List[List[int]]) -> None:
  #type1[0] giver liste over x af type 1
  #type1[1] giver liste over y af type 1
  #type2[0] giver liste over x af type 2
  #type2[1] giver liste over y af type 2

  #printer et plot over hvor de to typer er
  pass

def plotK (type1:List[List[int]]) -> None:
  #type1[0] giver liste over x
  #type1[1] giver liste over y

  #printer et plot over hvordan ændringer i k pævirker antal korekte
  pass