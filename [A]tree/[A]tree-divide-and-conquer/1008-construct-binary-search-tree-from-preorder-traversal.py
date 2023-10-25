# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        n = len(preorder)
        idx = 0

        def build_helper(lower, upper):
            nonlocal idx
            if idx >= n:
                return None
            val = preorder[idx]
            if val <= lower or val >= upper:
                return None
            node = TreeNode(val)
            idx += 1
            node.left = build_helper(lower, val)
            node.right = build_helper(val, upper)
            return node

        return build_helper(float('-inf'), float('inf'))
    
# time O(n)
# space O(n)
# using tree and divide and conquer and re-build BST (top-down approach) and dfs (preorder and recursive)
'''
1. use BST properties
2. preorder = ROOT + [LEFT SUB] + [RIGHT SUB]
            = ROOT + [ROOT OF LEFT SUB + REST ORF LEFT SUB] + [ROOT OF RIGHT SUB + REST ORF RIGHT SUB]
'''