# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int: 
#         curr_speed = ceil(sum(piles)/h)
#         max_piles = [pile for pile in piles if pile > curr_speed]
#         curr_turns = [ceil(pile/curr_speed) for pile in max_piles]
#         speed = sum(curr_turns) + (len(piles) - len(max_piles))
#         if speed > h:
#             curr_speed = ceil((speed/h) * curr_speed)
#         while speed > h:
#             max_piles = [pile for pile in piles if pile > curr_speed]
#             curr_turns = [ceil(pile/curr_speed) for pile in max_piles]
#             speed = sum(curr_turns) + (len(piles) - len(max_piles))
#             if speed > h:
#                 curr_speed = min(max_piles)
#                 min_index = max_piles.index(curr_speed)
#                 curr_speed = min(curr_speed, ceil(max_piles[min_index] / (curr_turns[min_index] - 1)))

                          
#         return curr_speed


import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        def canfinish(K):
            hours_needed = 0
            for p in piles:
                hours_needed+= ceil(p/K) #doing the cummulative sum
            return hours_needed <= h   
    
        # here we are taking k b/w the range of 1, max(piles)

            
        l = 1
        r = max(piles)
            
        while l<r:
            mid = (l+r)//2
                
            if canfinish(mid):# we are checking if we can finish with mid speed
                r = mid       #if yes then we will see if there is anything min than this 
                            # and the reason we are not making the r = mid -1 coz 
                            # then if our mid would be the required k then we might miss it.
            
            else:
                l = mid+1
                    
        return r

