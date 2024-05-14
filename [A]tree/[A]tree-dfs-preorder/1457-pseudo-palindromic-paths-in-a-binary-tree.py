# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        res = 0

        def valid(val):
            count = 0
            for i in range(1, 10):
                if val & (1 << i) != 0:
                    count += 1
            return count <= 1

        def dfs(node, val):
            nonlocal res
            if not node:
                return
            val ^= 1 << node.val
            if not node.left and not node.right:
                res += valid(val)
                return
            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, 0)
        return res

# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive) and bitmask 
# when masking notice difference of |, ^, &