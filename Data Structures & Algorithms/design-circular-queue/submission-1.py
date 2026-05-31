class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[-1]*k
        self.front = 0
        self.rear=-1
        self.n=0
        self.m=k

    def enQueue(self, value: int) -> bool:
        if self.n < self.m :
            if self.rear == self.m-1 :
                self.rear=0
            else:
                self.rear+=1
            self.queue[self.rear]=value
            self.n+=1
            return True 
        else:
            return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.front]=-1
            self.n-=1
            if self.front == self.m-1 :
                self.front=0
            else:
                self.front+=1
            return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]


    def isEmpty(self) -> bool:
        if self.n==0:
            return True
        else :
            return False

    def isFull(self) -> bool:
        if self.n == self.m:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()