# Definition for singly-linked list
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next

        while slow:
            if not fast or not fast.next:
                return False
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}
        while head:
            if nodes.get(head, 0):
                return True
            else:
                nodes[head] = True
            head = head.next
        
        return False
