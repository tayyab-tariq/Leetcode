# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #   Check if k nodes exist for reversal
        curr = head
        for _ in range(k):
            if not curr: 
                return head
            curr = curr.next
        
        #   Reverse k number of nodes
        prev = None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        #   curr contains remaing original nodes which are not reversed
        #   Point the tail node to reversed nodes
        #   head contains the tail node
        head.next = self.reverseKGroup(curr, k)
        
        return prev
