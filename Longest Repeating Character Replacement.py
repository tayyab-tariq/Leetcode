class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        
        left = 0
        res = 0
        maxf = 0
        
        for right in range(len(s)):
            window = right - left + 1
            char[s[right]] = 1 + char.get(s[right],0)
            
            maxf = max(maxf,char[s[right]])
            
            if window - maxf > k:
                char[s[left]] -= 1
                window -= 1
                left += 1
            
            res = max(res,window)
            
        return res 
