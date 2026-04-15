class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.head = self.Node(0, 0)
        self.trial = self.Node(0,0) 

        self.head.prev= self.trial
        self.trial.next = self.head

    def add(self , node) :
        prevNode=self.head.prev
        node.prev = prevNode
        node.next=self.head
        prevNode.next=node
        self.head.prev=node
    
    def remove(self , node) :
        prevNode = node.prev
        nextNode = node.next
        
        prevNode.next = nextNode
        nextNode.prev= prevNode


    def move_to_head(self , node ) :
        self.remove(node)
        self.add(node)
    def get(self, key: int) -> int:
        if key not in self.cache :
            return -1
        
        self.move_to_head(self.cache[key])
        return self.cache[key].value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.remove(self.cache[key])
            del self.cache[key]
        if len(self.cache) == self.capacity :
            del self.cache[self.trial.next.key]
            self.remove(self.trial.next)
        newNode=self.Node(key,value)
        self.add(newNode)
        self.cache[key]=newNode