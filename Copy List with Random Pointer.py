"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldCopy = {}

        curr = head
        while curr:
            node = Node(curr.val)
            oldCopy[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldCopy[curr]
            copy.next = oldCopy[curr.next] if curr.next else None
            copy.random = oldCopy[curr.random] if curr.random else None
            curr = curr.next
        
        return oldCopy[head] if head else head
