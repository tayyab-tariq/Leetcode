# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr, prev = head, None
        nodes = head

        for i in range(k):
            nodes = nodes.next
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head = prev
        while prev.next:
            prev = prev.next
        
        prev.next = nodes

        return head
            
