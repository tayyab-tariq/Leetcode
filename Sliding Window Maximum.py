class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # q = collections.deque()
        # r, l = 0, 0
        # while(r < len(nums)):
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()      
        #     q.append(r)

        #     if l > q[0]:
        #         q.popleft()

        #     if r+1 >= k:
        #         res.append(nums[q[0]])
        #         l += 1
        #     r += 1
        # return res

        stack, res = [], []
        left, right = 0, 0

        while right < len(nums):
            while stack and nums[stack[-1]] < nums[right]:
                stack.pop()
            stack.append(right)
        
            if left > stack[0]:
                stack.pop(0)
            
            if right+1 >= k:
                res.append(nums[stack[0]])
                left += 1
            
            right += 1
        
        return res
