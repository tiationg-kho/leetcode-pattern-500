# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        def get_next_leaf(stack):
            leaf = None
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    leaf = node
                    break
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return leaf

        stack1 = [root1]
        stack2 = [root2]
        while stack1 or stack2:
            leaf1 = get_next_leaf(stack1)
            leaf2 = get_next_leaf(stack2)
            if not leaf1 and not leaf2:
                continue
            if not leaf1 or not leaf2:
                return False
            if leaf1.val != leaf2.val:
                return False
        return True

# time O(n)
# space O(n)
# using tree and dfs (preorder and iterative)