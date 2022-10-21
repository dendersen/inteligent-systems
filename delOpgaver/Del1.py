#from plotingTools.point import Point
#from plotingTools.plotter import plot2
#from knn.testKNN import dataKnown1,dataKnown2,dataStart
#from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

#1. Lav en class Point, der repræsenterer et punkt som initialiseres et tilfældigt sted på skærmen 
# og som har en label i form af en farve (rød/blå eller kat/hund…). Dette udgør mængden
point_count = 10
x_point = [np.random.randint(1,20) for n in range(point_count)]
y_point = [np.random.randint(1,20) for n in range(point_count)]
x_red = []
y_red = []
x_blue = []
y_blue = []
for i in range(0,point_count):
  if i%2 == 1:
    x_red.append(x_point[i])
    y_red.append(y_point[i])
  if i%2 == 0:
    x_blue.append(x_point[i])
    y_blue.append(y_point[i])

plt.scatter(x_red,y_red,color='red')
plt.scatter(x_blue,y_blue,color='blue')
plt.show()
#2. Lav en liste af disse Point punkter og visualiser dem på skærmen med forskellige farver
