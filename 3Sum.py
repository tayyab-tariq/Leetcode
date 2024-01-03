class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right, target = i+1, len(nums)-1, 0-nums[i]
            while left < right:
                num = nums[left] + nums[right]
                if num > target:
                    right -= 1
                elif num < target:
                    left += 1
                else:
                    res.add((nums[left], nums[i], nums[right]))
                    left += 1
                    right -= 1


        return res
