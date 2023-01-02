class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            temp[i] = prefix
            prefix *= nums[i]
        
        # print(temp)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            # print(temp[i],postfix)
            temp[i] *= postfix
            # print(nums[i])
            postfix *= nums[i]
            
        return temp
        
