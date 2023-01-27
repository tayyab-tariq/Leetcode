class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = 1
        post = 1
        sets = [1] * length

        for i in range(length):
            sets[i] *= pre
            # print('Pre: ', i, pre,sets)
            pre = pre * nums[i]
            
            sets[length-i-1] *= post
            # print('Post: ', length-i-1, post,sets)
            post = post * nums[length-i-1]
            # print(pre, post, "\n")
            

        return sets
          
#         temp = [0] * len(nums)
        
#         prefix = 1
#         for i in range(len(nums)):
#             temp[i] = prefix
#             prefix *= nums[i]
        
#         # print(temp)
#         postfix = 1
#         for i in range(len(nums)-1,-1,-1):
#             # print(temp[i],postfix)
#             temp[i] *= postfix
#             # print(nums[i])
#             postfix *= nums[i]
            
#         return temp
        
