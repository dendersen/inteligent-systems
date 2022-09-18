from math import sqrt
from struct import pack
import struct
from typing import List
class Point:
  pass

class Point:
  def __init__(self,x:float,y:float) -> None:
    self.x:float = x
    self.y:float = y
  
  def distance(self,version:int,point:Point):
    dist = [self.euclid,self.manhattan,self.chebyshev,self.hammingManhattan,self.hammingEuclid,self.hammingChebyshev]
    return dist[version](point)
  
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
  return bin(struct.unpack("!i",struct.pack("!f",F))[0]).replace("0b","")

def dif(i:list,j:list):
  Dif = 0
  for l,L in zip(i,j):
    Dif += l != L
  return Dif

k = Point(1,2)
t = Point(3,4) 