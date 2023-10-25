# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def helper(node, cur_max):
            nonlocal res
            if not node:
                return
            if node.val >= cur_max:
                res += 1
                cur_max = node.val
            helper(node.left, cur_max)
            helper(node.right, cur_max)
        
        helper(root, float('-inf'))
        return res
    
# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive)