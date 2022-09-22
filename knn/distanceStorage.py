from plotingTools.point import Point

class Distance:
  def __init__(self,point:Point,distance:float) -> None:
    self.point = point
    self.distance = distance

def checkDist(dist:Distance):
  return dist.distance