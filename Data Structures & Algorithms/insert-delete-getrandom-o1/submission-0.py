import random
class RandomizedSet:

    def __init__(self):
        self.size=0
        self.st=set()
        self.lst=[]

    def insert(self, val: int) -> bool:
        if val in self.st:
            return False
        self.st.add(val)
        self.lst.append(val)
        self.size+=1
        return True

    def remove(self, val: int) -> bool:
        if val in self.st:
            self.lst.remove(val)
            self.st.remove(val)
            self.size-=1
            return True
        return False

    def getRandom(self) -> int:
        rand=random.randint(0,self.size-1)
        return self.lst[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()