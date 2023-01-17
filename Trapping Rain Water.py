class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        maxl = height[left]
        maxr = height[right]
        
        water = 0
        while left < right:
            if maxl <= maxr:
                left += 1;
                water += max(maxl-height[left],0)
                
                maxl = max(height[left],maxl)
                    
            else:
                right -= 1;
                water += max(maxr-height[right],0)
                
                maxr = max(height[right],maxr)
                
        return water
