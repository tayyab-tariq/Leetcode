class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr, low, high, target):
            if high >= low:
                mid = (high + low) // 2
                if arr[mid] < target:
                    return binary_search(arr, mid + 1, high, target)
                elif arr[mid] > target:
                    return binary_search(arr, low, mid - 1, target)
                else:
                    return mid
            else:
                return -1

        return binary_search(nums, 0, len(nums) - 1, target)
