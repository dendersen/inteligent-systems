from knn.testKNN import quick, quickData, quickRand, quickTrueData

def Test(result,expectedResult):
  if result == expectedResult:
    print("\u001b[32m [succes]\n")
  else:
    print("\u001b[31m [failed]\n")
    

while True:
  # quick()
  # quickRand(100,300,0,120,25)
  quickData(10000,0.5)
  # quickTrueData()

  if input ("done? ") == "yes":
    break