# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return (0, True)
            left_height, left_balance = dfs(node.left)
            right_height, right_balance = dfs(node.right)
            cur_height = max(left_height + 1, right_height + 1)
            cur_balance = left_balance and right_balance and abs(left_height - right_height) <= 1
            return (cur_height, cur_balance)

        return dfs(root)[1]
    
# time O(n), due to traverse
# space O(n), due to skewed tree's tree height (recursion stack)
# using tree and dfs (postorder and recursive)