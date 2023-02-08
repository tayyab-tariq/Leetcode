class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, left, maxf = 0, 0, 0
        freq = {}
        for r,chr in enumerate(s):
            freq[chr] = 1 + freq.get(chr, 0)
            maxf = max(maxf, freq[chr])            
            if ( (r-left+1) - maxf <= k):
                res += 1
            else:
                freq[s[left]] -= 1
                left += 1     
        return res
