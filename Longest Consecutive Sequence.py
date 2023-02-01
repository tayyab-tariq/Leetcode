class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        sort_nums = sorted(nums)

        if len(nums)>0:
            length = 1
            longest = 1
            for i in range(1,len(sort_nums)):
                if sort_nums[i]-1 == sort_nums[i-1]:
                    length += 1
                else:
                    longest = max(length,longest)
                    length = 1

            return max(length,longest)
        else:
            return 0

        
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for num in nums:
#             if num-1 not in numSet:
#                 length = 1
#                 while (num + length) in numSet:
#                     length += 1
                
#                 longest = max(length, longest)
            
#         return longest
           
