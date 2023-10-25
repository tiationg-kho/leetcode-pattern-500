# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        val_inorder_idx = {}
        for i, num in enumerate(inorder):
            val_inorder_idx[num] = i

        def build_helper(postorder_left_idx, postorder_right_idx, inorder_left_idx, inorder_right_idx, node_count):
            if node_count < 1:
                return None
            val = postorder[postorder_right_idx]
            node = TreeNode(val)
            inorder_mid_idx = val_inorder_idx[val]
            left_tree_count = inorder_mid_idx - inorder_left_idx
            right_tree_count = node_count - left_tree_count - 1
            node.left = build_helper(postorder_left_idx, postorder_left_idx + left_tree_count - 1, inorder_left_idx, inorder_mid_idx - 1, left_tree_count)
            node.right = build_helper(postorder_left_idx + left_tree_count, postorder_right_idx - 1, inorder_mid_idx + 1, inorder_right_idx, right_tree_count)
            return node

        return build_helper(0, n - 1, 0, n - 1, n)

# time O(n)
# space O(n)
# using tree and divide and conquer and re-build tree (top-down)
'''
postorder: last value is root
inorder: every value before root is left subtree, after root is right subtree
'''