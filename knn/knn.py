from plotingTools.point import Point as Point
from plotingTools.plotter import plot2,plot1
from typing import List




class Knn:
  def __init__(self,knownDataType:List[List[Point]],k:int = 5,distID:int = 0) -> None:
    self.k = k
    self.ori:List[List[Point]] = knownDataType#saves original know data, this ensures that you can run a test on multiple k
    self.Type:List[List[Point]] = knownDataType#contains all calculated points of differentTypes
    self.distanceCalcID = distID#which formula should be used to calculate distance
    self.numberOfTypes = len(knownDataType)
  
  def UpdateDataset(self,data:List[Point],solution:List[int] = -1)->None:
    if solution == -1:
      solution = [0]*(len(data))
      #in case no solution is give generates a buffer that is not meant to be read but can be read as a way to know results
    
    self.data = data #data pieces containing a list of points
    self.solution:List[int] = solution#solution to data piece of index x #true means type 1, false means type 2
    self.error = [False]*(len(self.solution))
    #self.solution[0] is the answer to self.data [0]
    self.kk:List[Point] = []#constains error numbers for different solutions
  
  def distance(self,item0:Point,item1:Point) -> int:
    return item0.distance(self.distanceCalcID,item1)#calls the distance method contained in the class point
  
  def runData(self,rang:range = -1) -> List[List[Point]]:#runs the algorithm through all unkown points
    if rang == -1:
      rang = range(0,len(self.data))#in case a range i not given the program will run through all points
    
    for i in rang:
      distType:List[List[int]] = [[]*self.numberOfTypes]*self.numberOfTypes#saves all types of points
      for l in range(0,self.numberOfTypes):
        for j in self.Type[l]:
          distType[l].append(self.distance(self.data[i],j))#finds distance to all known type 1
      for l in range(0,self.numberOfTypes):
        distType[l].sort()#sorts distances
      
      T = [0]*self.numberOfTypes #stores how far into the list points have been checked
      
      s = 0
      for j in range(0,self.k):
        if any(len(distType[t]) == T[t] for t in range(0,self.numberOfTypes)): #checks for more points
          break
        for t in range (1,self.numberOfTypes):
          if distType[t][T[t]] < distType[s][T[s]]:#finds nearest next point
            s = t
            T[s] #TODO
      self.Type[s].append(self.data[i])
      self.error[i] = s == self.solution
    return self.Type#returns the points of each type
  
  def visualize(self) -> None:#plots true and false as different items in a plot
    plot2(self.Type)
  
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
      k_nn = Knn([self.ori[0].copy(),self.ori[1].copy()],i)#creates a new knn algorithm with a new k
      k_nn.UpdateDataset(self.data.copy(),self.solution.copy())#provides the algorithem with data
      k_nn.runData()#runs the algorithm
      e = k_nn.errorRate()#checks the number of errors
      self.kk.append(Point(i,e))#saves the errors
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
