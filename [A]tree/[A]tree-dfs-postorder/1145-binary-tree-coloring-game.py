# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        res = False

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_count = dfs(node.left)
            right_count = dfs(node.right)
            if node.val == x:
                upper_count = n - left_count - right_count - 1
                second_player_count = max(upper_count, left_count, right_count)
                first_player_count = n - second_player_count
                res = second_player_count > first_player_count
            return left_count + right_count + 1

        dfs(root)
        return res
        
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive)