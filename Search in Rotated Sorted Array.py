class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            print(mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[left] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1