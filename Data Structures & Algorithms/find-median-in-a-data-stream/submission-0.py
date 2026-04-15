class MedianFinder:

    def __init__(self):
        self.listOfIntegers=[]
        self.size=0

    def addNum(self, num: int) -> None:
        if not self.listOfIntegers  :
            self.listOfIntegers.append(num)
            self.size+=1
        else :
            for i in range(self.size) :
                if self.listOfIntegers[i] >= num :
                    self.listOfIntegers.insert(i,num)
                    self.size+=1
                    return
            self.listOfIntegers.append(num)
            self.size+=1
    def findMedian(self) -> float:
        if self.size % 2 == 0 :
            return (self.listOfIntegers[self.size//2 - 1 ]+self.listOfIntegers[self.size//2])/2
        else :
            return self.listOfIntegers[self.size//2]