# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            node_as_peak_path = left_path + right_path + node.val
            res = max(res, node_as_peak_path)
            return max(left_path + node.val, right_path + node.val, 0)

        dfs(root)
        return res
        
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive)