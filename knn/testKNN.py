from typing import List
from main import Knn


def solutionGen(data:List[List],a:float = 0.2,b:float=-1.6,c:float=-0.3):
  sol = []
  for i in data:
    if i[1] > 0.2 * (i[0] ** 2) + i[0] ** (-1.6) - 0.3:
      sol.append(True)
    else:
      sol.append(False)
  return sol 

dataStart:List[List] =[[1,2],[5,6],[7,8],[9,10],[10,2],[3,7],[1,6],[7,5],[9,30],[8,28],[18,10],[2,26],[6,12],[19,20],[17,13],[4,18],[13,15],[8,4],[6,2],[10,7],[2,12],[14,30],[6,20],[6,16],[8,21],[2,23],[18,2],[20,7],[4,25],[12,20],[7,17],[14,26],[14,16],[6,24],[14,6],[4,21],[12,12],[1,31],[17,16],[4,14],[2,20],[15,11],[6,22],[2,17],[20,15],[16,19],[4,18],[5,10],[21,9],[16,6],[9,32],[4,31],[20,27],[16,30],[7,30],[14,22],[8,24],[6,12],[4,9],[4,28],[1,29],[9,27],[12,8],[20,19],[20,17],[20,5],[14,2],[20,12]]
solution = solutionGen(dataStart)
dataKnown1 = [[1,1],[3,3],[5,7],[15,46],[1,41],[3,13],[12,34],[7,20],[2,25],[7,30],[5,35],[2,4]]
dataKnown2 = [[1,0],[3,0],[5,4],[15,15],[14,14],[13,4],[12,26],[7,6],[7,1],[22,40]]


k = Knn(dataKnown1.copy(),dataKnown2.copy(),5)
k.UpdateDataset([dataStart.copy(),solution.copy()])
k.runData()
# k.visualize()
# k.visualizeSolution()
print(k.errorRate())

print (dataKnown1)
t = Knn(dataKnown1.copy(),dataKnown2.copy())
t.UpdateDataset([dataStart.copy(),solution.copy()])
t.testK(range(1,26,2))
t.visualizeK()

input("done")

