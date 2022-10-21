from random import randint
from typing import List
from sklearn.datasets import make_moons
from dataCollection import kommaSeperatedReader

from plotingTools.colorList import colors
from knn.knn import Knn
from plotingTools.point import Point
from plotingTools.randomData import randomPoints
from plotingTools.plotter import plotn
def solutionGen(data:List[Point],a:float = 0.2,b:float=-1.6,c:float=-0.3):
  sol = []
  for i in data:
    if i.y > a * (i.x ** 2) + i.x ** (b) + c:
      sol.append(colors[0])
    else:
      sol.append(colors[1])
  return sol 

def soll(data:List[Point],feet:bool = False,a:float = 0.2,b:float=-1.6,c:float=-0.3) -> List[Point]:
  for i in data:
    if i.y > a * (i.x ** 2) + i.x ** (b) + c:
      i.features[0] = colors[0]
    else:
      i.features[0] = colors[1]
  if feet:
    for i in data:
      if i.x > 10:
        i.features.append("help")
      else:
        i.features.append("good")
  return data 

dataStart:List[Point] = [Point(1,2),Point(5,6),Point(7,8),Point(9,10),Point(10,2),Point(3,7),Point(1,6),Point(7,5),Point(9,30),Point(8,28),Point(18,10),Point(2,26),Point(6,12),Point(19,20),Point(17,13),Point(4,18),Point(13,15),Point(8,4),Point(6,2),Point(10,7),Point(2,12),Point(14,30),Point(6,20),Point(6,16),Point(8,21),Point(2,23),Point(18,2),Point(20,7),Point(4,25),Point(12,20),Point(7,17),Point(14,26),Point(14,16),Point(6,24),Point(14,6),Point(4,21),Point(12,12),Point(1,31),Point(17,16),Point(4,14),Point(2,20),Point(15,11),Point(6,22),Point(2,17),Point(20,15),Point(16,19),Point(4,18),Point(5,10),Point(21,9),Point(16,6),Point(9,32),Point(4,31),Point(20,27),Point(16,30),Point(7,30),Point(14,22),Point(8,24),Point(6,12),Point(4,9),Point(4,28),Point(1,29),Point(9,27),Point(12,8),Point(20,19),Point(20,17),Point(20,5),Point(14,2),Point(20,12)]
dataKnown1 = [Point(1,1),Point(3,3),Point(5,7),Point(15,46),Point(1,41),Point(3,13),Point(12,34),Point(7,20),Point(2,25),Point(7,30),Point(5,35),Point(2,4)]
dataKnown2 = [Point(1,0),Point(3,0),Point(5,4),Point(15,15),Point(14,14),Point(13,4),Point(12,26),Point(7,6),Point(7,1),Point(22,40)]
def quick():
  solution = solutionGen(dataStart)
  k = Knn([*soll(dataKnown1.copy()),*soll(dataKnown2.copy())],3)
  k.UpdateDataset(dataStart.copy(),solution.copy())
  k.runData()
  k.visualize()
  k.visualizeSolution()
  print(k.errorRate())
  
  
  t = Knn([*soll(dataKnown1.copy()),*soll(dataKnown2.copy())],1,1)
  t.UpdateDataset(dataStart.copy(),solution.copy())
  t.testK(range(1,19,2))
  a = t.visualizeK()
  t.testDist(a)
  t.visualizeAll(7,6,True)

def quickData(numberOfPoints = 500,percentKnown:float = 0.5,Randomnes = 0.17):
  xy,colorID = make_moons(numberOfPoints,noise=Randomnes)
  
  xy = [i for i in xy]
  colorID = [i for i in colorID]
  
  unKnownList =[]
  solution = []
  for i in range(0,int(numberOfPoints*percentKnown)):
    index = randint(0,len(xy)-1)
    a = xy.pop(index)
    unKnownList.append(Point(a[0],a[1]))
    solution.append(colors[colorID.pop(index)])
  knownList = [Point(i[0],i[1],color=colors[j]) for i,j in zip(xy,colorID)]
  
  a = Knn(knownList)
  a.UpdateDataset(unKnownList,solution)
  a.runData()
  a.visualize()
  a.testK(range(1,14,2))
  a.visualizeSolution()
  b = a.visualizeK()
  a.testDist()
  a.visualizeAll(range(1,14,2))

def quickRand(numberOfKnownPoints:int,numberOfUnkownPoints:int,origin:float,tall:float,wide:float):
  known = randomPoints(numberOfKnownPoints,wide,origin,tall,origin)
  unknown = randomPoints(numberOfUnkownPoints,wide,origin,tall,origin)
  solution = solutionGen(unknown)
  
  k = Knn(soll(known),3,1)
  k.UpdateDataset(unknown,solution)
  k.runData()
  k.visualize()
  k.visualizeSolution()
  print(k.errorRate())
  
  
  t = Knn(soll(known))
  t.UpdateDataset(unknown,solution)
  t.testK(range(1,19,2))
  a = t.visualizeK()
  t.testDist(a)
  t.visualizeAll(7,6,True)

def quickTrueData():
  known = kommaSeperatedReader("testData\OccupiedTrain","csv")
  unKnown = kommaSeperatedReader("testData\OccupiedTest","csv")
  knownPoints = [Point(i[0],i[1],i[-1]) for i in known]
  unKnownPoints = [Point(i[0],i[1]) for i in unKnown]
  a = Knn(knownPoints)
  a.UpdateDataset(unKnownPoints,[i[-1] for i in unKnown])
  a.visualize()
  a.runData()
  a.visualize()
