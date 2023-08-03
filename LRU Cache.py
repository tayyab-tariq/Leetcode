class ListNode:
    def __init__(self, val: int, next: ListNode):
        self.val = val
        self.next = next



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = ListNode(0)
        
    def get(self, key: int) -> int:
        return -1

    def put(self, key: int, value: int) -> None:
        # if len(self.cache) > capacity:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = val

        self.count += 1    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
