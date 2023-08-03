# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) > 1:
            temp = None
            for i in range(1,len(lists)):
                list1 = lists[0]
                list2 = lists[i]

                lists[0] = self.mergeList(list1, list2)
                
        return lists[0]    

    def mergeList(self, list1: [ListNode], list2: [ListNode]) -> Optional[ListNode]:
        node = ListNode()
        tail = node

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next

                else:
                    tail.next = list2
                    list2 = list2.next

                tail = tail.next
            elif list1:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            elif list2:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
            
        return node.next
    
