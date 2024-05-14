# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return None, 0
            left_cand, left_depth = dfs(node.left)
            right_cand, right_depth = dfs(node.right)
            cur_cand, cur_depth = None, max(left_depth + 1, right_depth + 1)
            if left_depth == right_depth:
                cur_cand = node
            elif left_depth > right_depth:
                cur_cand = left_cand
            else:
                cur_cand = right_cand
            return cur_cand, cur_depth

        return dfs(root)[0]
    
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive)