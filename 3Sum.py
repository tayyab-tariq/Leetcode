class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)
        result = []
        for i, num in enumerate(sorted_list):
            if num > 0:
                break
            if i > 0 and num == sorted_list[i-1]:
                continue

            left, right = i + 1, len(sorted_list) - 1
            while left < right:
                target = num + sorted_list[left] + sorted_list[right]
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    result.append([num, sorted_list[left], sorted_list[right]])
                    left += 1
                    right -= 1
                    while sorted_list[left] == sorted_list[left - 1] and left < right:
                        left += 1
            
        
        return result

        
