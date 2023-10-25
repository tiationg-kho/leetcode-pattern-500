# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def helper(node, freq):
            nonlocal res
            if not node:
                return
                
            freq[node.val - 1] += 1

            if not node.left and not node.right:
                count = 0
                for i in range(9):
                    if freq[i] % 2:
                        count += 1
                if count <= 1:
                    res += 1
                return

            helper(node.left, freq[:])
            helper(node.right, freq[:])
        
        helper(root, [0 for _ in range(9)])
        return res

# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive)

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def helper(node, mask):
            nonlocal res
            if not node:
                return

            mask = mask ^ (1 << node.val)
            if not node.left and not node.right:
                count = 0
                for i in range(1, 10):
                    if mask & (1 << i):
                        count += 1
                if count <= 1:
                    res += 1
            helper(node.left, mask)
            helper(node.right, mask)

        helper(root, 0)
        return res
    
# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive) and bitmask 
# when masking notice difference of |, ^, &