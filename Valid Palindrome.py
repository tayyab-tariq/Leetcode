









# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
        
#         index = len(s)-1
#         for i in range(len(s)):
#             if not s[i].isalnum():
#                 continue
             
#             while not s[index].isalnum():
#                 index -= 1
            
#             if s[i] != s[index]:
#                 return False
            
#             index -= 1
            
#             if i > index:
#                 break
        
#         return True
