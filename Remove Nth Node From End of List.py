# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = head, head
        
        for i in range(n):
            curr = curr.next

        if not curr:
            return head.next
        
        while curr.next:
            prev = prev.next
            curr = curr.next
        
        prev.next = prev.next.next
        return head
        
        # prev, curr = None, head
        # temp = head
        # count = 0
        # while temp:
        #     count += 1
        #     temp = temp.next
        #     if count >= n+1:
        #         prev = curr
        #         curr = curr.next
        # if count == n:
        #     return head.next
        # else:
        #     if prev:
        #         if curr:
        #             prev.next = curr.next
        #         else:
        #             prev.next = None
        #     else:
        #         return None
        # return head
