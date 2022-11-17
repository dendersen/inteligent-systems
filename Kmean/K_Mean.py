from typing import List, Union
from plotingTools.point import Point
from plotingTools.randomData import randomPoints
from random import randint

class K_Mean:
  def __init__(self,Data:List[Point],k:int = 5,distID:int = 0) -> None:
    self.k = k
    self.ori:List[Point] = Data#saves original know data, this ensures that you can run a test on multiple k
    self.referencePoints:List[Point] = Data#contains all calculated points of differentTypes
    self.distanceCalcID = distID#which formula should be used to calculate distance
    # self.numberOfTypes = len(knownDataType) #no longer used
  
  def updateDataset(self):
    pass
  
  def run(self,maxIterations:int):
    startMean = []
    for i in range(0,self.k):
      startMean.append(self.referencePoints[randint(0,len(self.referencePoints))])
    
    
    for limit in range(0,maxIterations):
      pass
    pass

  def returnDist(t:tuple):
    return t[0]
  
  def DistributePoints(points:Point, means:Point)->List[List[Point]]:
    """_summary_

    Args:
        points (Point): the points to bedistributed
        means (Point): the means the points should be distributed between
    
    Returns:
        List[List[Point]]: the sorted points, the mean is the first index
    """
    
    pass
  
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