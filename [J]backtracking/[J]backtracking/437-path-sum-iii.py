# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        res = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(node, total):
            nonlocal res
            res += prefix_count[total - targetSum]
            prefix_count[total] += 1
            for child in [node.left, node.right]:
                if child:
                    dfs(child, total + child.val)
            prefix_count[total] -= 1
            
        if root:
            dfs(root, root.val)
        return res
    
# time O(n), due to dfs preorder traversal
# space O(n), due to prefix sum's hashamp
# using dfs and backtracking and prefix sum and backtracking with constraints
'''
1. the reason for backtracking prefix count is because we only care downward path
'''