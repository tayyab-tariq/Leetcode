class ListNode:
    def __init__(self, key:int, val: int, next = None):
        self.obj = {}
        self.obj[key] = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = ListNode(-1, 0)
        
    def get(self, key: int) -> int:
        # curr = self.head
        # while curr:
        #     print(curr.obj, key)
        #     curr = curr.next
        # print()

        temp = self.head
        prev = None
        while temp:
            if temp.obj.get(key,0):
                val = temp.obj.get(key,0)
                prev.next = temp.next
                tmp2 = self.head.next
                self.head.next = temp
                temp.next = tmp2
                return val
            prev = temp
            temp = temp.next
        return -1

    def put(self, key: int, value: int) -> None:
        if self.count >= self.capacity:
            temp = self.head
            prev = None
            while temp.next:
                prev = temp
                temp = temp.next
            prev.next = None
            temp = self.head.next

            self.head.next = ListNode(key, value, temp)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(key, value)

            self.count += 1 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
