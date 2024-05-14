# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0

        def build(min_val, max_val):
            nonlocal idx
            if idx == len(preorder):
                return None
            if preorder[idx] < min_val or preorder[idx] > max_val:
                return None
            node = TreeNode(preorder[idx])
            idx += 1
            node.left = build(min_val, node.val)
            node.right = build(node.val, max_val)
            return node
        
        return build(float('-inf'), float('inf'))
    
# time O(n)
# space O(n)
# using tree and divide and conquer and re-build BST (top-down approach) and dfs (preorder and recursive)
'''
1. use BST properties
2. preorder = ROOT + [LEFT SUB] + [RIGHT SUB]
            = ROOT + [ROOT OF LEFT SUB + REST ORF LEFT SUB] + [ROOT OF RIGHT SUB + REST ORF RIGHT SUB]
'''