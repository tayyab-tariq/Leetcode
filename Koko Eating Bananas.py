class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        curr_speed = ceil(sum(piles) / h)
        big_piles = [pile for pile in piles if pile > curr_speed]
        curr_turns = [ceil(pile / curr_speed) for pile in big_piles]
        curr_num_hours = (len(piles) - len(big_piles)) + sum(curr_turns)

        while curr_num_hours > h:
            next_speed = float("inf")
            for i in range(len(big_piles)):
                if curr_turns[i] > 1:
                    next_speed = min(next_speed, ceil(big_piles[i] / (curr_turns[i] - 1)))
            curr_speed = next_speed
           
            curr_turns = [ceil(pile / curr_speed) for pile in big_piles]
            curr_num_hours = (len(piles) - len(big_piles)) + sum(curr_turns)
        return curr_speed
