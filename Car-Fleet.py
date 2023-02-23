class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev = None
        count = 0
        pair = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        for p, s in pair:
            val = (target - p)/s
            if not prev or val > prev:
                prev = val
                count += 1
        
        return count
