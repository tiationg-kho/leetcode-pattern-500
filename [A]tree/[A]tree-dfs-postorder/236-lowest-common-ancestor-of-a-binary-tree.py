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
                return None
            left_cand = dfs(node.left)
            right_cand = dfs(node.right)
            if node.val == p.val or node.val == q.val:
                return node
            if left_cand and right_cand:
                return node
            if left_cand or right_cand:
                return left_cand or right_cand
            return None
        
        return dfs(root)
    
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive)
'''
1. dfs postorder (bottom up approach), helps to get the potential LCA info
'''