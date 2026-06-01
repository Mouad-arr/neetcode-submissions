class LFUCache:

    def __init__(self, capacity: int):
        self.data={}
        self.capacity=capacity
        self.timestamp=0
    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data[key][1]+=1
        self.timestamp+=1
        self.data[key][2]=self.timestamp
        return self.data[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity<=0:
            return
        self.timestamp+=1
        if key in self.data:
            self.data[key][0]=value
            self.data[key][1]+=1
            self.data[key][2]=self.timestamp
            return 
        if len(self.data)>=self.capacity :
            min_freq = float('inf')
            min_timestamp=float('inf')
            lfu_key=None
            for k,(_,freq,ts) in self.data.items():
                if freq < min_freq or (min_freq==freq and ts < min_timestamp) :
                    min_freq=freq
                    min_timestamp=ts
                    lfu_key=k
            if lfu_key is not None :
                del self.data[lfu_key]
        self.data[key]=[value,1,self.timestamp]        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)