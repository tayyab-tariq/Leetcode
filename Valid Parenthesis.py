class Solution:
    def isValid(self, s: str) -> bool:
        # open_bracket = {'[':']', '{':'}', '(':')'}        
        # brackets = []
        # for i in range(len(s)):
        #     if s[i] in open_bracket:
        #         brackets.append(open_bracket[s[i]])
        #     else:
        #         if brackets:
        #             if s[i] != brackets.pop():
        #                 return False
        #         else:
        #             return False

        # if brackets:
        #     return False

        # return True

        open_bracket = {'{':'}', '(':')', '[':']'}
        stack = []
        for bracket in s:
            if bracket in open_bracket.keys():
                stack.append(bracket)
            else:
                if stack:
                    closed = stack.pop()
                    if open_bracket.get(closed, 0) != bracket:
                        return False
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
