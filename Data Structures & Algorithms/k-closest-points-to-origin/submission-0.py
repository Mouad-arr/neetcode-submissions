import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points) :
            return points
        def distance(P) :
            return math.sqrt(pow(P[0],2)+pow(P[1],2))
        D={}
        for i,p in enumerate(points) :
            D[i]=distance(p)
        closest=(sorted(D.items(),key=lambda x : x[1]))
        L=list(points[i[0]] for i in closest )
        return L[:k]