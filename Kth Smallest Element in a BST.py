# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # bfs = [root]
        # res = []
        # while bfs:
        #     node = bfs.pop(0)
        #     if k > 0:
        #         res.append(node.val)
        #         k -= 1
        #         if k == 0:
        #             res = sorted(res)
        #     else:
        #         if res[-1] > node.val:
        #             res.pop()
        #             res.append(node.val)
        #             res = sorted(res)
        #     if node.left:
        #         bfs.append(node.left)
        #     if node.right:
        #         bfs.append(node.right)

        # return res[-1]

        res = []
        def inOrder(root):
            if not root:
                return

            inOrder(root.left)

            if len(res) == k:
                return
            res.append(root.val)

            inOrder(root.right)
        
        inOrder(root)
        return res[-1]


