class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        i,n=1,len(trips)
        trips.sort(key=lambda x: x[1])
        numPass=trips[0][0]
        tm=0
        while i<n :
            if numPass>capacity :
                return False
            while tm<i and  trips[tm][2]<=trips[i][1] :
                numPass-=trips[tm][0]
                tm+=1
            numPass+=trips[i][0]
            i+=1
        if numPass > capacity :
            return False
        return True
            