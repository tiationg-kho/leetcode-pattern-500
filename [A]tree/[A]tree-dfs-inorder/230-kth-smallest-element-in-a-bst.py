# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0
        res = - 1

        def dfs(node):
            nonlocal idx, res
            if not node:
                return
            dfs(node.left)
            idx += 1
            if k == idx:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res
        
# time O(n), for skewed tree's height
# space O(n), due to memo stack's size for skewed tree's height 
# using tree and dfs (inorder and recursive)