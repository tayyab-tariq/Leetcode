class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i in range(len(nums)):
        difference = target - nums[i]
        if nums[i] in mapp.keys():
            return [mapp.get(nums[i],0), i]
        mapp[difference] = i
            
        # for i,n in enumerate(nums):
        #     difference = target - n
        #     if difference in mapp:
        #         return [mapp[difference], i]
        #     mapp[n] = i
        
        
     
