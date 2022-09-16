import math
from readline import append_history_file
import plotter
from typing import List


class knn:
  def __init__(self,knownDataType1:List[List[int]],knownDataType2:List[List[int]],k:int = 5) -> None:
    self.k = k
    self.Type1:List[List[int]] = knownDataType1
    self.Type2:List[List[int]] = knownDataType2
  
  def dataSet(self,data):
    self.data = data[0] #n dimension list. list 1 = data pieces containing a list 2 = features
    self.solution = data[1]#solution to data piece of index x
    #self.solution[0] is the answer to self.data [0]
  
  def distance(self,item0,item1) -> int:
    return math.sqrt(self.distCalc(self.data[item0],self.data[item1]))
  
  def distCalc(self,arr0:list,arr1:list) -> int:
    if type(arr0) != type(arr1): 
      print (TypeError(),"incorrect dimensionel length in array",arr0,arr1)
      return -1
    if(type(arr0[0]) == int):
      for i,j in zip(arr0,arr1):
        out += (i,j)**2
    else:
      for i,j in zip(arr0,arr1):
        out += self.distCalc(i,j)
    return out
  
  def runData(self,rang:range):
    for i in rang:
      distType1 = []
      distType2 = []
      for j in self.Type1:
        distType1.append(self.distance(self.data[i],j))
      for j in self.Type2:
        distType2.append(self.distance(self.data[i],j))
      distType1.sort()
      distType2.sort()
      T1,T2 = 0
      for j in range(0,self.k):
        if distType1(T1) < distType2(T2):
          T1 += 1
        else:
          T2 += 1
      if T1 > T2:
        self.Type1.append(self.data[i])
      else:
        self.Type2.append(self.data[i])
    