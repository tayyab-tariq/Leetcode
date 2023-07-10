class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        heights.append(0)

        for i,h in enumerate(heights):
            if stack and h == stack[-1][1]:
                continue
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index
            stack.append((start, h))
        
        # for i,h in stack:
        #     area = max(area, h * (len(heights) - i))
        
        return area

            
