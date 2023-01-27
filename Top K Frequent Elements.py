class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num,0)

        elements = []

        for i in range(k):
            max_freq = -1
            for key, value in frequency.items():
                if frequency[key] >= max_freq:
                    if key not in elements:
                        number = key
                        max_freq = frequency[key]
            elements.append(number)
            frequency[number] = -1
        
        return elements
    
#         count = {}
#         freq = [[] for i in range(len(nums)+1)]
        
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
            
#         for n, c in count.items():
#             freq[c].append(n)
        
#         res = []
#         for i in range(len(freq) - 1,-1,-1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
                
            
    
