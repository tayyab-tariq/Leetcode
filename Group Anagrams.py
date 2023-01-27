import collections
class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}

        for words in strs:
            word = tuple(sorted(words))
            if word in groupings.keys():
                groupings[word].append(words)
            else:
                groupings[word] = []
                groupings[word].append(words)

        return groupings.values()
    
#         grouped = collections.defaultdict(list)        
#         for i in strs:
#             sort = " ".join(sorted(i))
#             # print(sort,i)
#             grouped[sort].append(i)
#         return grouped.values()
            
