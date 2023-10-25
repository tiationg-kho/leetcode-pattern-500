# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def build_helper(node):
            if not node:
                return ''
            cur = str(node.val)
            left = build_helper(node.left)
            right = build_helper(node.right)
            if not left and not right:
                return cur
            elif left and right:
                return cur + '(' + left + ')' + '(' + right + ')'
            elif not left and right:
                return cur + '()' + '(' + right + ')'
            else:
                return cur + '(' + left + ')'

        return build_helper(root)
    
# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive) and turn tree to string