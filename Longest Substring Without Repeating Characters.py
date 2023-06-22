class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        # i, length, longest = 0, 0, 0
        # char = {}
        # while i < len(s):
        #     if char.get(s[i],-1) == -1:
        #         char[s[i]] = i
        #         length += 1
        #     else:
        #         longest = max(length,longest)
        #         length = 0
        #         i = char[s[i]]
        #         char = {}
        #     i += 1

        # return max(length, longest)
