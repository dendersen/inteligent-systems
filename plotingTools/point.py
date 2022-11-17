from math import sqrt
from struct import pack,unpack
from typing import List
from plotingTools.colorList import colors
class Point:pass

class Point:
  def __init__(self,x:float,y:float,color:str = "lime",FeatureList:List = [],z:float=0,erga:float = 0,olga:float = 0,mean:Point = None) -> None:
    if type(color)==int:
      color = colors[color]
    self.z = z
    self.x:float = x
    self.y:float = y
    self.features = [color,*FeatureList]
    self.dist = [self.euclid,self.manhattan,self.chebyshev,self.hammingManhattan,self.hammingEuclid,self.hammingChebyshev]
    self.erga:float = erga
    self.olga:float = olga
    self.mean = mean
  
  def attachMean(self,mean:Point)->Point:
    """adds mean to point

    Args:
        mean (Point): the  mean to witch the point is attached

    Returns:
        Point: self
    """
    self.mean = mean
    return self
  
  def distance(self,version:int,point:Point):
    return self.dist[version](point)
  
  def euclid(self,point:Point)->float:
    return sqrt((self.x-point.x)**2 + (self.y-point.y)**2 + (self.z-point.z)**2 + (self.erga-point.erga)**2 + (self.olga-point.olga)**2)
  
  def manhattan(self,point:Point)->float:
    return abs(self.x-point.x) + abs(self.y-point.y) + abs(self.z-point.z) + abs(self.erga-point.erga) + abs(self.olga-point.olga)
  
  def chebyshev(self,point:Point)->float:
    return max(abs(self.x - point.x),abs(self.y - point.y),abs(self.z - point.z),abs(self.erga - point.erga),abs(self.olga - point.olga))
  
  def hamming(self,point:Point) -> List[int]:
    x1 = floatToBin(self.x)
    y1 = floatToBin(self.y)
    z1 = floatToBin(self.z)
    erga1 = floatToBin(self.erga)
    olga1 = floatToBin(self.olga)
    x2 = floatToBin(point.x)
    y2 = floatToBin(point.y)
    z2 = floatToBin(point.z)
    erga2 = floatToBin(point.erga)
    olga2 = floatToBin(point.olga)
    diffx = dif(x1,x2)
    diffy = dif(y1,y2)
    diffz = dif(z1,z2)
    differga = dif(erga1,erga2)
    diffolga = dif(olga1,olga2)
    return [diffx,diffy,diffz,differga,diffolga]
  
  def hammingManhattan(self,point:Point)->float:
    diff = self.hamming(point)
    return diff[0] + diff[1] + diff[2] + diff[3] + diff[4]
  
  def hammingEuclid(self,point:Point):
    diff = self.hamming(point)
    return sqrt(diff[0]**2 + diff[1]**2 + diff[2]**2 + diff[3]**2 + diff[4]**2)
  
  def hammingChebyshev(self,point:Point):
    diff = self.hamming(point)
    return max(diff[0],diff[1],diff[2],diff[3],diff[4])

def floatToBin(F:float)->str:
  return bin(unpack("!i",pack("!f",F))[0]).replace("0b","")

def dif(i:list,j:list):
  Dif = 0
  for l,L in zip(i,j):
    Dif += l != L
  return Dif  