
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def dfs(root, level):
            if not root:
                return None
            
            if len(values) < level:
                values.append(root.val)

            right = dfs(root.right, level+1)
            left = dfs(root.left, level+1)

        if root:
            values.append(root.val)
            dfs(root, 1)

        return values
        
        # if not root:
        #     return []
        # right = self.rightSideView(root.right)
        # left = self.rightSideView(root.left)
        # return [root.val] + right + left[len(right):]

