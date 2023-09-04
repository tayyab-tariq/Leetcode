# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_num):
            if not root:
                return 0
            
            res = 1 if root.val >= max_num else 0
                
            max_num = max(root.val, max_num)
            res += dfs(root.left, max_num)
            res += dfs(root.right, max_num)
            a
            return res

        return dfs(root, root.val)
