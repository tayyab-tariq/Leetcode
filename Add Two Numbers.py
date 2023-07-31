# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        count = 0
        while l1 or l2:
            if not l1:
                val = l2.val + count
                count -= 1
                count = max(count, 0)
                l2 = l2.next
            elif not l2:
                val = l1.val + count
                count -= 1
                count = max(count, 0)
                l1 = l1.next
            else:
                val = l1.val + l2.val + count
                count -= 1
                count = max(count, 0)
                l1 = l1.next
                l2 = l2.next

            if val > 9:
                count += 1
                val = val%10

            temp.val = val
            prev = temp
            temp.next = ListNode()
            temp = temp.next

        if count > 0:
            prev.next.val = count
        else:
            prev.next = None
        return head
