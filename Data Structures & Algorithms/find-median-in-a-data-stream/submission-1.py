class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        if self.large and self.large[0] < -self.small[0] :
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small) :
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-val)
        elif len(self.large) + 1 < len(self.small) :
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        
    def findMedian(self) -> float:
        if len(self.large) > len(self.small) :
            return self.large[0]
        if len(self.small) > len(self.large) :
            return -self.small[0]
        return ( self.large[0] - self.small[0] ) / 2 