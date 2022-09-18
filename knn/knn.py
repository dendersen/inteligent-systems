from plotingTools.point import Point as Point
from plotingTools.plotter import plot2,plot1
from typing import List




class Knn:
  def __init__(self,knownDataType1:List[Point],knownDataType2:List[Point],k:int = 5,distID = 0) -> None:
    self.k = k
    self.ori = [knownDataType1,knownDataType2]
    self.Type1:List[Point] = knownDataType1
    self.Type2:List[Point] = knownDataType2
    self.distanceCalcID = distID
  
  def UpdateDataset(self,data:List[Point],solution:List[bool] = -1):
    if solution == -1:
      solution = [False]*(len(data))
    self.data = data #list 1 = data pieces containing a list 2 = features
    self.solution:List[bool] = solution#solution to data piece of index x #true means type 1, false means type 2
    self.error = [False]*(len(self.solution))
    #self.solution[0] is the answer to self.data [0]
    self.kk = []
  
  def distance(self,item0:Point,item1:Point) -> int:
    return item0.distance(self.distanceCalcID,item1)
  
  def runData(self,rang:range = -1) -> List[List[Point]]:
    if rang == -1:
      rang = range(0,len(self.data))
    
    for i in rang:
      distType1:List[int] = []
      distType2:List[int] = []
      for j in self.Type1:
        distType1.append(self.distance(self.data[i],j))
      for j in self.Type2:
        distType2.append(self.distance(self.data[i],j))
      distType1.sort()
      distType2.sort()
      T1,T2 = 0,0
      for j in range(0,self.k):
        if len(distType2) - 1 == T2 and len(distType1) - 1 == T1:
          break
        if len(distType1) - 1 == T1:
          T2 += 1
        elif len(distType2) -1 == T2:
          T1 += 1
        elif distType1[T1] < distType2[T2]:
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
    plot2(self.Type1,self.Type2)
  
  def errorRate(self)->int:
    e = 0
    for i in self.error:
      if i:
        e += 1
    return e
  
  def testK(self,rangeOfK: range = -1)->List[List[int]]:
    if rangeOfK == -1 :
      rangeOfK = range(1,8,2)
    
    for i in rangeOfK:
      k_nn = Knn(self.ori[0].copy(),self.ori[1].copy(),i)
      k_nn.UpdateDataset(self.data.copy(),self.solution.copy())
      k_nn.runData(-1)
      e = k_nn.errorRate()
      self.kk.append([i,e])
    return self.kk
  
  def visualizeK(self)->None:
    if len(self.kk) < 2:
      print("testk() has not run, checking stardard k's")
      self.testK(-1)
    plot1([*zip(*self.kk)])
  
  def visualizeSolution(self):
    Type1 = self.ori[0]
    Type2 = self.ori[1]
    
    for j,i in zip(self.solution,self.data):
      if j:
        Type1.append(i)
      else:
        Type2.append(i)
    plot2(Type1,Type2)
