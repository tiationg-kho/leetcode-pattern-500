# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def copy(node):
            if not node:
                return None
            new_node = TreeNode(node.val)
            new_node.left = copy(node.left)
            new_node.right = copy(node.right)
            return new_node

        def build_helper(left, right):
            if left > right:
                return [None]
            res = []
            for root_val in range(left, right + 1):
                left_trees = build_helper(left, root_val - 1)
                right_trees = build_helper(root_val + 1, right)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = copy(left_tree)
                        root.right = copy(right_tree)
                        res.append(root)
            return res

        return build_helper(1, n)
        
# time O(Catalan(n))
# space O(Catalan(n))
# using tree and divide and conquer and unique BST