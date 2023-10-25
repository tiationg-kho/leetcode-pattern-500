# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return (0, 0)
            left_count, left_total = dfs(node.left)
            right_count, right_total = dfs(node.right)
            cur_count = left_count + right_count + 1
            cur_total = left_total + right_total + node.val
            res = max(res, cur_total / cur_count)
            return (cur_count, cur_total)

        dfs(root)
        return res

# time O(n)
# space O(n)
# using tree and dfs (postoder, recursive)