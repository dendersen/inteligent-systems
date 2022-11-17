from typing import List, Union
from plotingTools.point import Point
from plotingTools.colorList import colors
from plotingTools.randomData import randomPoints
from random import randint

class K_Mean:
  def __init__(self,Data:List[Point],k:int = 5,distID:int = 0) -> None:
    self.k = k
    self.ori:List[Point] = Data#saves original know data, this ensures that you can run a test on multiple k
    self.referencePoints:List[Point] #contains all calculated points with a stored mean
    self.distanceCalcID = distID#which formula should be used to calculate distance
    # self.numberOfTypes = len(knownDataType) #no longer used
    self.means:List[Point]=[]
  
  def updateDataset(self):
    pass
  
  def run(self,maxIterations:int)->None:
    """runs the algorithem

    Args:
        maxIterations (int): the number of runs to find mean

    Raises:
        Exception: if a points is missing raises exception
    """
    for i in range(0,self.k):
      self.means.append(self.ori[randint(0,len(self.ori)-1)])
    self.referencePoints = self.DistributePoints(self.ori,self.means)
    self.means = [self.FindMean(i) for i in self.sortBySharedMean(self.referencePoints)]
    self.referencePoints = self.DistributePoints(self.ori,self.means)
    
    for limit in range(0,maxIterations):
      sortedmeans = self.sortBySharedMean(self.referencePoints)
      self.means = [self.FindMean(i) for i in sortedmeans]
      temp = self.DistributePoints(self.referencePoints,self.means)
      if len(self.referencePoints) != len(temp):#checks if points are missing
        raise Exception("missing points")

  def returnDist(t:tuple):
    return t[0]
  
  def DistributePoints(self,points:List[Point], means:List[Point])->List[Point]:
    """distributes points between means

    Args:
        points (Point): the points to bedistributed
        means (Point): the means the points should be distributed between
    
    Returns:
        List[List[Point]]: the sorted points, the mean is the first index
    """
    distributedPoints:List[Point] = []
    allMenas=[]
    for p in points:
      dist:tuple = (0,1e100)
      for l,i in enumerate(means):
        distance = p.distance(self.distanceCalcID,i)
        if(distance < dist[1]):
          dist = (l,distance)
      allMenas.append(means[dist[0]])
      distributedPoints.append(p.attachMean(means[dist[0]]))
    return distributedPoints
  
  def FindMean(self,points:List[Point])->Point:
    """finds a new mean
    
    Args:
        points (List[Point]): points to witch a mean should be found
    
    Returns:
        Point: the mean of the given points
    """
    x = [i.x for i in points]
    y = [i.y for i in points]
    z = [i.z for i in points]
    xMean = sum(x)/len(x)
    yMean = sum(y)/len(y)
    zMean = sum(z)/len(z)
    return Point(xMean,yMean,z=zMean)
  
  def sortBySharedMean(self,points:List[Point])->List[List[Point]]:
    temp = []
    temp2:List[List[Point]] = []
    for i in points:
      if(not i.mean.contains(temp)):
        temp.append(i.mean)
        print(len(temp))
        temp2.append([i])
      else:
        for l,j in enumerate(temp):
          if(j == i.mean):
            temp2[l].append(i)
            break
          else:
            pass
        else:
          raise Exception("?")
    return temp2
  
  def colorBook(self):
    for i,j in  enumerate(self.sortBySharedMean(self.referencePoints)):
      for l in j:
        l.features[0] = i