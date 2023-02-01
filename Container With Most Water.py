class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height)-1
        i = 0
        max_area = 0
        
        while i < end:
            area = min(height[i], height[end]) * (end - i)
            max_area = max(area, max_area)

            if height[i] < height[end]:
                i += 1
            else:
                end -= 1
            
        return max_area


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         water = 0
#         left = 0
#         right = len(height)-1
        
#         while left < right:
#             minimum = min(height[right],height[left])
#             area = (right-left) * minimum
            
#             water = max(area,water)
            
#             if height[left]>height[right]:
#                 right -= 1
#             else:
#                 left += 1
                
#         return water
