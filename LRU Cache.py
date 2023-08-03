class ListNode:
    def __init__(self, val: int, next: ListNode):
        self.val = val
        self.next = next



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        
    def get(self, key: int) -> int:
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # if len(self.cache) > capacity:
            
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
