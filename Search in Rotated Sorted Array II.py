class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[right]:        #   Can not determine which side is sorted
                right -= 1

            elif nums[mid] < nums[right]:       # Right side is sorted
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:   # Left side of mid is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False
