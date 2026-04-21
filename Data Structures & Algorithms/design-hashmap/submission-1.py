class MyHashMap:

    def __init__(self):
        self.values=[]
        self.keys=[]

    def put(self, key: int, value: int) -> None:
        if key in self.keys :
            self.values[self.keys.index(key)]=value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        if key in self.keys :
            return self.values[self.keys.index(key)]
        else:
            return -1
    def remove(self, key: int) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            del self.values[index]
            del self.keys[index]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)