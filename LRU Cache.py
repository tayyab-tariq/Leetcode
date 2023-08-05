class Node:
def __init__(self, k, v):
    self.key = k
    self.val = v
    self.prev = None
    self.next = None

class LRUCache:
def __init__(self, capacity):
    self.capacity = capacity
    self.dic = dict()
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

def get(self, key):
    if key in self.dic:
        n = self.dic[key]
        return n.val
    return -1

def set(self, key, value):])
    n = Node(key, value)
    self.dic[key] = n
    if len(self.dic) > self.capacity:
        n = self.head.next
        del self.dic[n.key]

def _remove(self, node):
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p

def _add(self, node):
    p = self.tail.prev
    p.next = node
    self.tail.prev = node
    node.prev = p
    node.next = self.tail
