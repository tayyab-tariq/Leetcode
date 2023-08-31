
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level_order = []
        local = [root]
    
        while local:
            ans = []
            for i in range(len(local)):
                node = local.pop(0)
                ans.append(node.val)

                if node.left:
                    local.append(node.left)
                if node.right:
                    local.append(node.right)
            level_order.append(ans)
        
        return level_order
                
