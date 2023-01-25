class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        longest = 0
        occured = set()
        for i in range(len(s)):
            if i == 0:
                longest = 1
            if i+1<len(s) and s[i]!=s[i+1]:
                index = i
                while(index < len(s)):
                    if s[index] in occured:
                        longest = max(length,longest)
                        length = 0
                        occured = set()
                        break

                    occured.add(s[index])
                    length += 1
                    index += 1        
        return max(length,longest)
