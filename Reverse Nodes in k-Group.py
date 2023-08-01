# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr, prev = head, None
        count = 0
        temp = curr
        while curr:
            if (count+1) % k == 0 and k > 1 and curr:          
                if count == 1:
                    tmp = curr.next
                    temp.next = curr.next
                    curr.next = temp
                    head = curr
                    curr = temp
                    temp = temp.next
                else:
                    print(prev.val, curr.val, temp.val)
            

            prev = curr
            curr = curr.next
            count += 1

        return head
            
