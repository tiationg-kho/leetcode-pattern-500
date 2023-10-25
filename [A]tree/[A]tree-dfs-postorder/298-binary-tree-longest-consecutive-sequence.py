# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0, float('-inf')
            left_len, left_val = dfs(node.left)
            right_len, right_val = dfs(node.right)
            cur_len = 1
            if left_val - 1 == node.val:
                cur_len = max(cur_len, left_len + 1)
            if right_val - 1 == node.val:
                cur_len = max(cur_len, right_len + 1)
            res = max(res, cur_len)
            return cur_len, node.val

        dfs(root)
        return res
    
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive)