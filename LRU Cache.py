class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None
    

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        return -1
    
    def put(self, key, value):
        node = Node(key, value)
