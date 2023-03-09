import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        left, right = 1, max(piles)
        min_speed = max(piles)

        def chkSpeed(piles, speed, h):
            count = 0
            for num in piles:
                if speed > num:
                    count += 1
                else:
                    val = math.ceil(num / speed)
                    count += val

            if count <= h:
                return True
            else:
                return False


        while left <= right:
            mid = (left + right) // 2
            chk = chkSpeed(piles, mid, h)
            if chk:
                min_speed = min(mid, min_speed)
                right = mid - 1
            else:
                left = mid + 1
            
        return min_speed
