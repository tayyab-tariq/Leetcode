class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while i >=0:
            if length > 0 and s[i] == ' ':
                break

            if s[i] != ' ':
                length += 1
            i -= 1

        return length


        # wordlist = s.split()
        # if wordlist:
        #     return len(wordlist[-1])
        # return 0
