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
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        curr = head
        second = prev
        while second:
            temp, temp1 = curr.next, second.next
            curr.next = second
            second.next = temp
            curr, second = temp, temp1

        return head
