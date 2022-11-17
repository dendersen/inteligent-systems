from Kmean.K_Mean import K_Mean
from knn.testKNN import dataStart
from plotingTools.plotterNew import Plot2D

a = K_Mean(dataStart)
a.run(2)
a.colorBook()
for  i in a.referencePoints:
  print(i.asCsv("hello","Data.csv"))

Plot2D([])