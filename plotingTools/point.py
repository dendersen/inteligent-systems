from math import sqrt
from struct import pack,unpack
from typing import List
from plotingTools.colorList import colors
class Point:
  pass

class Point:
  def __init__(self,x:float,y:float,color:str = "lime",FeatureList:List = []) -> None:
    if type(color)==int:
      color = colors[color]
    self.x:float = x
    self.y:float = y
    self.features = [color,*FeatureList]
    self.dist = [self.euclid,self.manhattan,self.chebyshev,self.hammingManhattan,self.hammingEuclid,self.hammingChebyshev]
  
  def distance(self,version:int,point:Point):
    return self.dist[version](point)
  
  def euclid(self,point:Point)->float:
    return sqrt((self.x-point.x)**2 + (self.y-point.y)**2)
  
  def manhattan(self,point:Point)->float:
    return abs(self.x-point.x) + abs(self.y-point.y)
  
  def chebyshev(self,point:Point)->float:
    return max(abs(self.x - point.x),abs(self.y - point.y))
  
  def hamming(self,point:Point) -> List[int]:
    x1 = floatToBin(self.x)
    y1 = floatToBin(self.y)
    x2 = floatToBin(point.x)
    y2 = floatToBin(point.y)
    diffx = dif(x1,x2)
    diffy = dif(y1,y2)
    return [diffx,diffy]
  
  def hammingManhattan(self,point:Point)->float:
    diff = self.hamming(point)
    return diff[0] + diff[1]
  
  def hammingEuclid(self,point:Point):
    diff = self.hamming(point)
    return sqrt(diff[0]**2 + diff[1]**2)
  
  def hammingChebyshev(self,point:Point):
    diff = self.hamming(point)
    return max(diff[0],diff[1])

def floatToBin(F:float)->str:
  return bin(unpack("!i",pack("!f",F))[0]).replace("0b","")

def dif(i:list,j:list):
  Dif = 0
  for l,L in zip(i,j):
    Dif += l != L
  return Dif