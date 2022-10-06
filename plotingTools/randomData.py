from typing import List
from random import random
from plotingTools.point import Point


def randomPoints(numberOfPoints:int,maxX,minX,maxY,minY):
  points:List[Point] = []
  for i in range(0,numberOfPoints):
    p = Point(random()*(maxX-minX)+minX,
    random()*(maxY-minY)+minY)
    points.append(p)
  return(points)