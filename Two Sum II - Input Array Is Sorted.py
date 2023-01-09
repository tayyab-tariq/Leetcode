class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index = len(numbers)-1
        i = 0    
    
        while i < index:
            if numbers[i]+numbers[index] > target:
                index -= 1
            elif numbers[i]+numbers[index] < target:
                i += 1
            else:
                return [i+1,index+1]
