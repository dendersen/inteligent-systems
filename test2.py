from sklearn.datasets import make_moons
from Kmean.K_Mean import K_Mean
from knn.testKNN import dataStart
from plotingTools.plotterNew import Plot2D
from plotingTools.plotter import plotn
from plotingTools.colorList import colors
from plotingTools.point import Point

a = K_Mean(dataStart)
a.run(20)
a.colorBook()

plotn(a.referencePoints)

xy,colorID = make_moons(500,noise=0.14)
xy = [i for i in xy]
colorID = [i for i in colorID]
knownList = [Point(i[0],i[1],color=colors[j]) for i,j in zip(xy,colorID)]

a = K_Mean(knownList)
a.run(20)
a.colorBook()
plotn(a.referencePoints)

for  i in a.referencePoints:
  print(i.asCsv("hello","Data.csv"))
Plot2D()

