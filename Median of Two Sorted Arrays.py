class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        length = len1 + len2
        mid = (length // 2) + 1

        p1, p2 = 0, 0
        prev, curr = 0, 0
        stack = []
        
        for i in range(mid):
            if p1 == len1:
                prev = curr
                curr = nums2[p2]
                p2 += 1

            elif p2 == len2:
                prev = curr
                curr = nums1[p1]
                p1 += 1

            elif nums1[p1] < nums2[p2]:
                prev = curr
                curr = nums1[p1]
                p1 += 1
            else:
                prev = curr
                curr = nums2[p2]
                p2 += 1

        if length % 2 == 0:
            return (prev+curr)/2
        else:
            return curr
