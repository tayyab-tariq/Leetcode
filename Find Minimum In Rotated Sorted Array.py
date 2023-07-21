class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        target = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
            target = min(nums[mid], target)
        
        return min(nums[right], target)
