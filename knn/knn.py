from plotingTools.point import Point as Point
from plotingTools.plotter import plot2,plot1
from typing import List, Tuple




class Knn:
  def __init__(self,knownDataType1:List[Point],knownDataType2:List[Point],k:int = 5,distID = 0) -> None:
    self.k = k
    self.ori = [knownDataType1,knownDataType2]#saves original know data, this ensures that you can run a test on multiple k
    self.Type1:List[Point] = knownDataType1#contains all calculated points of type 1
    self.Type2:List[Point] = knownDataType2#contains all calculated points of type 2
    self.distanceCalcID = distID#which formula should be used to calculate distance
  
  def UpdateDataset(self,data:List[Point],solution:List[bool] = -1)->None:
    if solution == -1:
      solution = [False]*(len(data))
      #in case no solution is give generates a buffer that is not meant to be read but can be read as a way to know results
    
    self.data = data #data pieces containing a list of points
    self.solution:List[bool] = solution#solution to data piece of index x #true means type 1, false means type 2
    self.error = [False]*(len(self.solution))
    #self.solution[0] is the answer to self.data [0]
    self.kk = []#constains error numbers for different solutions
  
  def distance(self,item0:Point,item1:Point) -> int:
    return item0.distance(self.distanceCalcID,item1)#calls the distance method contained in the class point
  
  def runData(self,rang:range = -1) -> List[List[Point]]:#runs the algorithm through all unkown points
    if rang == -1:
      rang = range(0,len(self.data))#in case a range i not given the program will run through all points
    
    for i in rang:
      distType1:List[int] = []#saves all type 1 points
      distType2:List[int] = []#saves all type 1 points
      for j in self.Type1:
        distType1.append(self.distance(self.data[i],j))#finds distance to all known type 1
      for j in self.Type2:
        distType2.append(self.distance(self.data[i],j))#finds distance to all known type 1
      
      distType1.sort()#sorts distances
      distType2.sort()
      
      T1,T2 = 0,0#
      
      for j in range(0,self.k):
        if len(distType2) - 1 == T2 or len(distType1) - 1 == T1: #checks for more points
          break
        if distType1[T1] < distType2[T2]: #finds nearest next point
          T1 += 1
        else:
          T2 += 1
      if T1 > T2: #saves result and checks for errors
        self.Type1.append(self.data[i])
        self.error[i] = not self.solution[i]#if solution is true (meant to be type 1) it will write false (no error) if not it writes true (error present), opposit if result is type 2
      else:
        self.Type2.append(self.data[i])
        self.error[i] = self.solution[i]
    
    return[self.Type1,self.Type2]#returns the points of type 1 and 2
  
  def visualize(self) -> None:#plots true and false as different items in a plot
    plot2(self.Type1,self.Type2)
  
  def errorRate(self)->int:#counts the number of True in error array
    e = 0
    for i in self.error:
      if i:
        e += 1
    return e
  
  def testK(self,rangeOfK: range = -1)->List[List[int]]:#test's for different k's on the current ori(original know points) and currently active dataset 
    if rangeOfK == -1 :#sets a default range of k
      rangeOfK = range(1,8,2)
    
    for i in rangeOfK:
      k_nn = Knn(self.ori[0].copy(),self.ori[1].copy(),i)
      k_nn.UpdateDataset(self.data.copy(),self.solution.copy())
      k_nn.runData(-1)
      e = k_nn.errorRate()
      self.kk.append([i,e])
    return self.kk
  
  def visualizeK(self)->None:
    if len(self.kk) < 1:
      print("testk() has not run, checking stardard k's")
      self.testK(-1)
    plot1([*zip(*self.kk)])
  
  def visualizeSolution(self)->None:
    Type1 = self.ori[0]
    Type2 = self.ori[1]
    
    for j,i in zip(self.solution,self.data):
      if j:
        Type1.append(i)
      else:
        Type2.append(i)
    plot2(Type1,Type2)
