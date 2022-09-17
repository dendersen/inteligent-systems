import math
import plotter as plotter
from typing import List


class Knn:
  def __init__(self,knownDataType1:List[List[int]],knownDataType2:List[List[int]],k:int = 5) -> None:
    self.k = k
    self.ori = [knownDataType1,knownDataType2]
    self.Type1:List[List[int]] = knownDataType1
    self.Type2:List[List[int]] = knownDataType2
  
  def UpdateDataset(self,data:List[List]):
    self.data = data[0] #n dimension list. list 1 = data pieces containing a list 2 = features
    self.solution:List[bool] = data[1]#solution to data piece of index x #true means type 1, false means type 2
    self.error = [False]*len(self.solution)
    self.kk = []
    #self.solution[0] is the answer to self.data [0]
  
  def UpdateDataset1(self,data:List,solv:List = -1):
    if solv ==-1:
      solv = [False]*len(data)
    self.data = data #n dimension list. list 1 = data pieces containing a list 2 = features
    self.solution:List[bool] = solv#solution to data piece of index x #true means type 1, false means type 2
    self.error = [False]*len(self.solution)
    self.kk = []
    #self.solution[0] is the answer to self.data [0]
  
  def distance(self,item0,item1) -> int:
    a = self.distCalc(self.data[item0],item1)
    return math.sqrt(abs(a))
  
  def distCalc(self,arr0:list,arr1:list) -> int:
    out = 0
    if type(arr0) != type(arr1): 
      print (TypeError(),"incorrect dimensionel length in array",arr0,arr1)
      return -1
    if(type(arr0[0]) == int):
      for i,j in zip(arr0,arr1):
        out += (i-j)**2
    else:
      for i,j in zip(arr0,arr1):
        out += self.distCalc(i,j)
    return out
  
  def runData(self,rang:range = -1) -> List[List[List[int]]]:
    if rang == -1:
      rang = range(0,len(self.data))
    
    for i in rang:
      distType1 = []
      distType2 = []
      for j in self.Type1:
        distType1.append(self.distance(i,j))
      for j in self.Type2:
        distType2.append(self.distance(i,j))
      distType1.sort()
      distType2.sort()
      T1,T2 = 0,0
      for j in range(0,self.k):
        if distType1[T1] < distType2[T2]:
          T1 += 1
        else:
          T2 += 1
      if T1 > T2:
        self.Type1.append(self.data[i])
        self.error[i] = not self.solution[i]
      else:
        self.Type2.append(self.data[i])
        self.error[i] = self.solution[i]
    
    return(self.Type1,self.Type2)
  
  def visualize(self) -> None:
    plotter.plot([*zip(*self.Type1)],[*zip(*self.Type2)])
  
  def errorRate(self)->int:
    e = 0
    for i in self.error:
      if i:
        e += 1
    print(e)
    return e
  
  def testK(self,rangeOfK: range = -1,rangeOfData:range = -1)->List[List[int]]:
    if rangeOfK == -1 :
      rangeOfK = range(1,8,2)
    
    for i in rangeOfK:
      k_nn = Knn(self.ori[0],self.ori[1],i)
      k_nn.UpdateDataset1(self.data,self.solution)
      k_nn.runData(rangeOfData)
      e = k_nn.errorRate()
      print(i,e)
      self.kk.append([i,e])
    return self.kk
  
  def visualizeK(self)->None:
    if len(self.kk) < 2:
      self.testK(range(1,8,2))
    plotter.plotK([*zip(*self.kk)])
  
  def visualizeSolution(self):
    Type1 = self.ori[0]
    Type2 = self.ori[1]
    
    for j,i in zip(self.solution,self.data):
      if j:
        Type1.append(i)
      else:
        Type2.append(i)
    plotter.plot([*zip(*Type1)],[*zip(*Type2)])
