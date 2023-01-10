import numpy as np
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = np.sort(nums)
        arr = []
        
        for i,num in enumerate(nums):
            if i>0 and nums[i-1]==num:
                continue
                
            i,j = i+1,len(nums)-1
            
            while i<j:
                triplet = num + nums[i] + nums[j]
                if triplet>0:
                    j-=1
                elif triplet<0:
                    i+=1
                else:
                    arr.append([num,nums[i],nums[j]])
                    i+=1
                    while nums[i] == nums[i-1] and i<j:
                        i+=1
                        
        return arr
        
