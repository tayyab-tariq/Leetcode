class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted_list = sorted(nums)
        # result = []
        # for i, num in enumerate(sorted_list):
        #     if num > 0:
        #         break
        #     if i > 0 and num == sorted_list[i-1]:
        #         continue

        #     left, right = i + 1, len(sorted_list) - 1
        #     while left < right:
        #         target = num + sorted_list[left] + sorted_list[right]
        #         if target < 0:
        #             left += 1
        #         elif target > 0:
        #             right -= 1
        #         else:
        #             result.append([num, sorted_list[left], sorted_list[right]])
        #             left += 1
        #             right -= 1
        #             while sorted_list[left] == sorted_list[left - 1] and left < right:
        #                 left += 1
            
        
        # return result

        sorted_nums = sorted(nums)
        result = set()

        for i, num in enumerate(sorted_nums):
            if num > 0:
                return result
            left, right = i+1, len(sorted_nums)-1
            while left < right:
                target = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if target == 0:
                    result.add(tuple([sorted_nums[i], sorted_nums[left], sorted_nums[right]]))
                    left += 1
                    right -= 1

                elif target < 0:
                    left += 1
                else:
                    right -= 1

        return result

        
