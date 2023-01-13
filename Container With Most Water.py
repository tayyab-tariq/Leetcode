class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            minimum = min(height[right],height[left])
            area = (right-left) * minimum
            
            water = max(area,water)
            
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
                
        return water
