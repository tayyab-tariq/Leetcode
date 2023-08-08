# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], count = 0) -> int:
        if not root:
            return count
        countl, countr = 0, 0
        if root.left:
            countl = max(self.maxDepth(root.left, count + 1), countl)            
        if root.right:
            countr = max(self.maxDepth(root.right, count + 1), countr)

        return max(countl, countr)
