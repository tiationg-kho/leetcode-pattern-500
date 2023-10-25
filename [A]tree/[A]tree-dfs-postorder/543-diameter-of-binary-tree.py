# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            node_as_peak = left_path + right_path
            res = max(res, node_as_peak)
            return max(left_path + 1, right_path + 1)

        dfs(root)
        return res
        
# time O(n), due to traverse
# space O(n), due to tree height for skewed tree
# using tree and dfs (postorder, recursive)