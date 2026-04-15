class CountSquares:

    def __init__(self):
        self.points=[]

    def add(self, point: List[int]) -> None:
        self.points.append(point)
    def distance(self,p1,p2):
        return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    def count(self, point: List[int]) -> int:
        if len(self.points)<3:
            return 0
        pointsV=[]
        pointsH=[]
        for p in self.points :
            if point[0]==p[0] and point[1]!=p[1]:
                pointsH.append(p)
            elif point[1]==p[1] and point[0]!=p[0]:
                pointsV.append(p)
        if len(pointsV)==0 or len(pointsH)==0:
            return 0
        ways=0
        for pv in pointsV:
            for ph in pointsH :
                if self.distance(ph,point)==self.distance(pv,point):
                    d=self.distance(ph,point)
                    for p in self.points :
                        if d==self.distance(p,pv) and d==self.distance(p,ph) and ( p[0]!=point[0] and p[1]!=point[1]):
                            ways+=1
        return ways