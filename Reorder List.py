# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while slow:
            if not fast or not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
        
        
        prev = slow.next = None
        slow = slow.next
        while second:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        print(head)
        print(prev)
        # curr = head
        
        # while prev:
        #     temp, temp2 = curr.next, prev.next
        #     curr.next = prev
        #     prev.next = curr
        #     curr, prev = temp, temp2
        
        return head
