from typing import List, Union
from plotingTools.point import Point
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
      self.means.append(self.ori[randint(0,len(self.ori))])
    self.referencePoints = self.DistributePoints(self.ori,self.means)
    self.means = self.FindMean(self.referencePoints)
    self.referencePoints = self.DistributePoints(self.ori,self.means)
    
    for limit in range(0,maxIterations):
      self.means = self.FindMean(self.referencePoints)
      temp = self.DistributePoints(self.referencePoints,self.means)
      if len(self.referencePoints) == len(temp):#checks if points are missing
        raise Exception("missing points")

  def returnDist(t:tuple):
    return t[0]
  
  def DistributePoints(self,points:List[Point], means:Point)->List[Point]:
    """distributes points between means

    Args:
        points (Point): the points to bedistributed
        means (Point): the means the points should be distributed between
    
    Returns:
        List[List[Point]]: the sorted points, the mean is the first index
    """
    distributedPoints:List[Point] = []
    for p in points:
      dist:tuple = (0,1e100)
      for l,i in enumerate(means):
        distance = p.distance(self.distanceCalcID,i)
        if(distance < dist[1]):
          dist = (l,distance)
      distributedPoints.append(p.attachMean(means))
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