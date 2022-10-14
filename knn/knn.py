from plotingTools.point import Point as Point
from plotingTools.plotter import plotn,plot1,plot3D
from plotingTools.colorList import colors
import knn.distanceStorage as dist
from typing import List, Union
from itertools import count

class Knn:
  def __init__(self,knownDataType:List[Point],k:int = 5,distID:int = 0,solutionKnown:bool = False) -> None:
    self.k = k
    self.ori:List[Point] = knownDataType#saves original know data, this ensures that you can run a test on multiple k
    self.referencePoints:List[Point] = knownDataType#contains all calculated points of differentTypes
    self.distanceCalcID = distID#which formula should be used to calculate distance
    # self.numberOfTypes = len(knownDataType) #no longer used
    self.line = solutionKnown
  
  def UpdateDataset(self,data:List[Point],solution:Union[List[str], str] = "lime")->None:
    if type(solution) == str:
      solution = [solution]*(len(data))
      #in case no solution is give generates a buffer that is not meant to be read but can be read as a way to know results
    
    self.data = data #data pieces containing a list of points
    self.solution:List[str] = solution#solution to data piece of index x #true means type 1, false means type 2
    self.error = [False]*(len(self.solution))
    #self.solution[0] is the answer to self.data [0]
    self.calcK:List[Point] = []#constains error numbers for different solutions
    self.calcD:List[Point] = []#constains error numbers for different solutions
    self.calcA:List[Point] = []#constains error numbers for different solutions
  
  def distance(self,item0:Point,item1:Point) -> int:
    return item0.distance(self.distanceCalcID,item1)#calls the distance method contained in the class point
  
  def runData(self) -> None:#runs the algorithm through all unkown points
    for test in self.data: #datapoint being checked
      distances:List[dist.Distance] = self.calculateDistance(test)
      
      distances.sort(key=dist.checkDist)
      
      feat = []
      for i,ll in zip (count(),test.features):
        cc = [l[1].point.features[i] for l in zip(range(0,self.k),distances)]#farverne af de nærmeste punkter
        
        c = self.activeFeatures(cc)
        Dist = [[cc.count(j),j] for j in c]#antal af hver farve
        Dist.sort(key=dist.colCheck)
        feat.append(Dist[0][1])
      
      test.features = feat
      self.referencePoints.append(test)
    # return self.referencePoints#returns the points of each type
      # test.color = colors[cc[1]]#saves colored point
      # self.referencePoints.append(test)
      # colorCheck:List[int] = [0] * len(colors)#typing list (color based)
      # for j in range(0,self.k):
      #    for I,l in enumerate(colors):
      #     if distances[j].point.color == l:#finds nearest color 
      #       colorCheck[I] += 1
      #       break
      
      # cc = [colorCheck[0],0]
      # for t,i in enumerate(colorCheck):#finds the index with the highest value
      #   if i > cc[0]:
      #     cc = [i,t]
      
      
      # cc = [l.point.color for j,l in zip(range(0,self.kk),distances)]
      
      # dist = [[cc.count(j),j] for j in colors]
      # dist.sort()
    #   distType:List[List[int]] = [[]*self.numberOfTypes]*self.numberOfTypes#saves all types of points
    #   for l in range(0,self.numberOfTypes):
    #     for j in self.referencePoints[l]:
    #       distType[l].append(self.distance(self.data[i],j))#finds distance to all known type 1
    #   for l in range(0,self.numberOfTypes):
    #     distType[l].sort()#sorts distances
    #   T = [0]*self.numberOfTypes #stores how far into the list points have been checked
    #   s = 0
    #   for j in range(0,self.k):
    #     if any(len(distType[t]) == T[t] for t in range(0,self.numberOfTypes)): #checks for more points
    #       break
    #     for t in range (1,self.numberOfTypes):
    #       if distType[t][T[t]] < distType[s][T[s]]:#finds nearest next point
    #         s = t
    #         T[s]
    #   self.referencePoints[s].append(self.data[i])
    #   self.error[i] = s == self.solution
    return
  
  def activeFeatures(self, cc) -> List[str]:
    for i in cc:
      col = []
      t = False
      for j in col:
        if j == i:
          t = True
          break
      if not t:
        col.append(i)
    return col

  def calculateDistance(self, test:Point) -> List[dist.Distance]:
    distances:List[dist.Distance] = []
    
    for j in self.referencePoints:
      if j != test:
        distances.append(dist.Distance(j,self.distance(test,j)))#calculate the distance
    return distances
  
  def visualize(self) -> None:#plots true and false as different items in a plot
    plotn(self.referencePoints,True,self.line,"k-værdien er " + str(self.k))
  
  def errorRate(self)->int:#counts the number of True in error array
    e=0
    for i,j in zip(self.referencePoints[::-1],self.solution[::-1]):
      if i.features[0] != j:
        e+=1
    return e
  
  def testK(self,rangeOfK: range = -1) -> List[Point]:#test's for different k's on the current ori(original know points) and currently active dataset 
    if rangeOfK == -1 :#sets a default range of k
      rangeOfK = range(1,8,2)
    
    for i in rangeOfK:
      self.calcK.append(self.buildInternalKNN(i,self.distanceCalcID))
    return self.calcK
  
  def visualizeK(self)->int:
    if len(self.calcK) < 1:
      print("testk() has not run, checking stardard k's")
      self.testK(-1)
    plot1(self.calcK)
    return min(self.calcK, key = self.visKey).x
  
  def visKey(self,point:Point):
    return point.y

  def visualizeSolution(self)->None:
    solv = self.ori
    
    for i,j in zip(self.referencePoints[::-1].copy(),self.solution[::-1]):
      i.features[0] = j
    plotn(solv,False,self.line,"Teoretisk rigtig løsning")

  def testDist(self,k:int = 5):
    print(k)
    for i in range(0,len(Point(0,0).dist)):
        self.calcD.append(self.buildInternalKNN(k,i,1))
    plot1(self.calcD,self.line,'Presition med k værdien ' + str(k) + ' (Antal fejl angivet over punkt)',"afstands funktion")

  def visualizeAll(self,Ksearch:int,DistSearch:int = len(Point(0,0).dist),evenK:bool = False):
    if evenK:
      self.__visAll(range(1,Ksearch+1),range(0,DistSearch))
    else:
      self.__visAll(range(1,Ksearch+1,2),range(0,DistSearch))
  
  def __visAll(self,Ksearch:range,DistSearch:range):
    for i in Ksearch:
      for j in DistSearch:
        self.calcA.append(self.buildInternalKNN(i,j,2))
    plot3D(self.calcA)

  def buildInternalKNN(self, k, dist, simple = 0):
      k_nn = Knn([*self.ori.copy()],k,dist)#creates a new knn algorithm with a new k and dist
      k_nn.UpdateDataset(self.data.copy(),self.solution.copy())#provides the algorithem with data
      k_nn.runData()#runs the algorithm
      e = k_nn.errorRate()#checks the number of errors
      if simple == 0:
        return (Point(k,e,"Lime",[],dist))#returns the errors
      if simple == 1:
        return (Point(dist,e,"Lime",[],k))
      if simple == 2:
        return (Point(k,dist,"Lime",[],e))
