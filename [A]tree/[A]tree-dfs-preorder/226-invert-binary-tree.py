# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
            
# time O(n)
# space O(n)
# using tree and dfs (preorder and iterative)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return node
            node.left, node.right = node.right, node.left
            helper(node.left)
            helper(node.right)
            return node
        
        return helper(root)

# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive)