from typing import List
from plotingTools.point import Point


def loadFile(fileName: str, fileExtention: str):#finder et text dokument og giver en string
  with open(fileName + "." + fileExtention) as f:
    text = f.read()
  return text

data:List[Point] = []

for i in loadFile("dataFromSheet","txt").split("\n"):
  j = i.split(",")
  if(j[0].isdecimal(),j[2].isdecimal(),j[3].isdecimal()):
    p = Point(
      float(j[0]),
      float(j[1]),
      j[2],
      [3]
    )
    data.append(p)