# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        for _ in range(2):
            if not curr:
                return head
            curr = curr.next
        
        prev, curr = None, head
        for _ in range(2):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        second = prev
        while second.next:
            second = second.next
        
        second.next = self.swapPairs(curr)

        return prev
                
