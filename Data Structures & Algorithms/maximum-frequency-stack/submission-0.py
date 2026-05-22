class FreqStack:

    def __init__(self):
        self.stack=[]
        self.mp={}
        self.m=0

    def push(self, val: int) -> None:
        self.stack.insert(0,val)
        if val not in self.mp:
            self.mp[val]=1
            self.m=max(self.m,1)
        else :
            self.mp[val]+=1
            self.m=max(self.m,self.mp[val])

    def pop(self) -> int:
        se=set()
        for key in self.mp :
            if self.mp[key]==self.m:
                se.add(key)
        if len(se)==1:
            for v in se :
                self.mp[v]-=1
                self.m-=1
                self.stack.remove(v)
                return v
        else :
            for k in self.stack :
                if k in se :
                    self.mp[k]-=1
                    self.stack.remove(k)
                    return k

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()