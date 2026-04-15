class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store : 
            self.store[key]=[(value,timestamp)]
        else :
            self.store[key].append((value,timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store : 
            return ""
        else : 
            L=self.store[key]
            left,right=0,len(L)-1
            res=""
            while left <= right :
                m=(left+right)//2
                # if L[right][1] <= timestamp:
                #     return L[right][0]
                if L[m][1] > timestamp :
                    right=m-1
                elif L[m][1] <= timestamp  :
                    left=m+1
                    res=L[m][0]
            return res 

