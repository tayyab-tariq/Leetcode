import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        curr_speed = ceil(sum(piles)/h)
        max_piles = [pile for pile in piles if pile > curr_speed]
        curr_turns = [ceil(pile/curr_speed) for pile in max_piles]
        speed = sum(curr_turns) + (len(piles) - len(max_piles))
        if speed > h:
            curr_speed = ceil((speed/h) * curr_speed)
        while speed > h:
            max_piles = [pile for pile in piles if pile > curr_speed]
            curr_turns = [ceil(pile/curr_speed) for pile in max_piles]
            speed = sum(curr_turns) + (len(piles) - len(max_piles))
            if speed > h:
                curr_speed = min(max_piles)
                min_index = max_piles.index(curr_speed)
                curr_speed = min(curr_speed, ceil(max_piles[min_index] / (curr_turns[min_index] - 1)))

                          
        return curr_speed
