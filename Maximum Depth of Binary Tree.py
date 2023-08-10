# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], count = 0) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)

    # def maxDepth(root, depth):            #        BFS
        #     if not root:
        #         return depth
            
        #     queue = [(root, 1)]
        #     while queue:
        #         node, depth = queue.pop(0)
        #         if node.left:
        #             queue.append((node.left, depth + 1))
        #         if node.right:
        #             queue.append((node.right, depth + 1))                
        #     return depth

        # return maxDepth(root, 0)

