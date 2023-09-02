class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(len(nums)):
            subsets = []
            for j in range(len(res)):
                subset = res[j] + [nums[i]]
                subsets.append(subset)
            res.extend(subsets)
        return res
