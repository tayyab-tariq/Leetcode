class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charS1 = Counter(s1)
        charS2 = {} 
        count, left, right = 0, 0, 0
        while right < len(s2):
            if charS1.get(s2[right], 0):
                if charS1.get(s2[right], 0) > charS2.get(s2[right], 0):
                    count += 1
                charS2[s2[right]] = 1 + charS2.get(s2[right], 0)
            
            if count == len(s1):
                if count == len(s1) and (right - left + 1) == len(s1):
                        return True
                while left <= right and count == len(s1):
                    if count == len(s1) and (right - left + 1) == len(s1):
                        return True
                    else:
                        if charS2.get(s2[left],0):
                            charS2[s2[left]] -= 1
                            if charS1.get(s2[left], 0) > charS2.get(s2[left], 0):
                                count -= 1 
                        left += 1
            right += 1

        # print(charS1, charS2)
        return False 
            
