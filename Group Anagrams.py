import collections
class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = collections.defaultdict(list)        
        for i in strs:
            sort = " ".join(sorted(i))
            # print(sort,i)
            grouped[sort].append(i)
        return grouped.values()
            
