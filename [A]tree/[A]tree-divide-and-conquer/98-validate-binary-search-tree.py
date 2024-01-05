# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid_helper(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return valid_helper(node.left, lower, node.val) and valid_helper(node.right, node.val, upper)

        return valid_helper(root, float('-inf'), float('inf'))
        
# time O(n), n is the number of nodes (traverse)
# space O(n), n is the recursive stack size (imagine an one branch tree)
# using tree and divide and conquer and two branch top-down and bst