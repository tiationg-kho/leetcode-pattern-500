# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None, 0
            left_cand, left_find = dfs(node.left)
            right_cand, right_find = dfs(node.right)
            if node.val == p.val or node.val == q.val:
                return node, left_find + right_find + 1
            if left_cand and right_cand:
                return node, left_find + right_find
            if left_cand:
                return left_cand, left_find
            if right_cand:
                return right_cand, right_find
            return None, 0

        res, find = dfs(root)
        return res if find == 2 else None
             
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive)