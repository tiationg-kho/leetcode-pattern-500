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
                return (0, None)
            left_height, left_cand = dfs(node.left)
            right_height, right_cand = dfs(node.right)
            cur_height = max(left_height + 1, right_height + 1)
            if left_height == right_height:
                cur_cand = node
            elif left_height > right_height:
                cur_cand = left_cand
            else:
                cur_cand = right_cand
            return (cur_height, cur_cand)

        return dfs(root)[1]
    
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive)