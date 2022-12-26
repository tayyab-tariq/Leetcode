class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for number in nums:
            if number in arr:
                return True
            arr.add(number)
                
        return False
