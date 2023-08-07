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
        if key in self.dict.keys():
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1
    
    def put(self, key, value):
        node = Node(key, value)
        if key in self.dict.keys():
            self._remove(self.dict[key])

        self._add(node)
        self.dict[key] = node

        if len(self.dict) > self.capacity:
            temp = self.head.next
            self._remove(temp)
            del self.dict[temp.key]
        
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        self.tail.prev = node
        node.next = self.tail
