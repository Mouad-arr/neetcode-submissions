class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def fleet(s,p,cars) :
            i=p.index(max([p[i] for i in range(len(p)) if i not in cars]))
            t=(target-p[i])/s[i]
            R=[]
            for j in range(len(s)) :
                if j not in cars : 
                    T=(target-p[j])/s[j]
                    if T<=t:
                        R.append(j)
            return R
        cars=[]
        n=len(speed)
        c=0
        while len(cars) != n :
            R=fleet(speed,position,cars)
            cars.extend(R)
            c+=1
        return c