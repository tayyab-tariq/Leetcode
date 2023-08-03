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

        while list1 and list2:
            if list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next

                else:
                    tail.next = list2
                    list2 = list2.next

                tail = tail.next
        
        if list1 or list2:
            tail.next = list1 if list1 else list2
            
        return node.next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None
#         if len(lists) == 1:
#             return lists[0]
#         mid = len(lists) // 2
#         l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
#         return self.merge(l, r)
    
#     def merge(self, l, r):
#         dummy = p = ListNode()
#         while l and r:
#             if l.val < r.val:
#                 p.next = l
#                 l = l.next
#             else:
#                 p.next = r
#                 r = r.next
#             p = p.next
#         p.next = l or r
#         return dummy.next
    
