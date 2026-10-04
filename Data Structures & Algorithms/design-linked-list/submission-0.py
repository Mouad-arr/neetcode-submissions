class MyLinkedList:

    def __init__(self):
        self.lst = []
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size :
            return -1
        return self.lst[index]

    def addAtHead(self, val: int) -> None:
        self.lst.insert(0,val)
        self.size+=1

    def addAtTail(self, val: int) -> None:
        self.lst.append(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size :
            return 
        self.lst.insert(index,val)
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<self.size :
            del self.lst[index]
            self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)