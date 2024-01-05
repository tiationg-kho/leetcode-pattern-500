# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete_helper(node):
            if not node:
                return node
            if node.val == key:
                if not node.left:
                    return node.right
                pred = node.left
                while pred and pred.right:
                    pred = pred.right
                pred.right = node.right
                return node.left
            elif node.val < key:
                node.right = delete_helper(node.right)
            else:
                node.left = delete_helper(node.left)
            return node

        return delete_helper(root)
        
# time O(n), due to tree height, can be logn
# space O(n), due to recursive stack
# using tree and divide and conquer and bst