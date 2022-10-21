from typing import List
from plotingTools.point import Point


def loadFile(fileName: str, fileExtention: str)->str:#finder et text dokument og giver en string
  with open(fileName + "." + fileExtention) as f:
    text = f.read()
  return text

data:List[Point] = []
for i in loadFile("testData/dataFromSheet","txt").split("\n"):
  j = i.split(",")
  if(j[0].isdecimal(),j[2].isdecimal(),j[3].isdecimal()):
    if float(j[0] == 0):
      j[0]+= 1e-10
    if float(j[1] == 0):
      j[1 ]+= 1e-10
    p = Point(
      float(j[0]),
      float(j[1]),
      j[2],
      [3]
    )
    data.append(p)

def kommaSeperatedReader(name:str,extension:str) -> List[List[float]]:
  out = []
  for l,i in enumerate(loadFile(name,extension).split("\n")):
    temp=[]
    for t,j in enumerate(i.split(",")):
      try:
        # print("read succes")
        temp.append(float(j))
      except:
        print(f"error, cannot read   \"{j}\"   will write {-1}\nfound on line nr.{l}, segment nr.{t}\nfile \"{name}.{extension}\"")
        temp.append(float(-1))
    # print(len(temp),l)
    out.append(temp)
  return out