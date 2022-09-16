from main import knn





k = knn([[1,1],[1,1],[1,1],[2,2],[2,2],[2,2]],[[6,6],[6,6],[6,6],[10,10],[10,10],[10,10]],1)
k.UpdateDataset([[[1,2],[3,4],[5,6],[7,8],[9,10],[1,2],[3,4],[5,6],[7,8],[9,10]],[True,True,True,True,False,False,False,False,False,False]])
k.runData(range(0,3))
k.visualize()
print(k.errorRate())


