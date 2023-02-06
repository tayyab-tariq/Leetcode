class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length, longest = 0,0
        
        chk = {}
        i = 0
        while i < len(s):
            if chk.get(s[i], -1) >= 0:
                i = chk[s[i]] + 1
                longest = max(longest, length)
                length = 0
                chk = {}
            else:
                length += 1
                chk[s[i]] = i
                i += 1
        
        return max(longest, length)
