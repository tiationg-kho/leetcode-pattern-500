# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        val_postorder_idx = {}
        for i, num in enumerate(postorder):
            val_postorder_idx[num] = i

        def build_helper(preorder_left_idx, preorder_right_idx, postorder_left_idx, postorder_right_idx, node_count):
            if node_count < 1:
                return None
            val = preorder[preorder_left_idx]
            node = TreeNode(val)
            if node_count == 1:
                return node
            postorder_left_tree_idx = val_postorder_idx[preorder[preorder_left_idx + 1]]
            left_tree_count = postorder_left_tree_idx - postorder_left_idx + 1
            right_tree_count = node_count - left_tree_count - 1
            node.left = build_helper(preorder_left_idx + 1, preorder_left_idx + left_tree_count, postorder_left_idx, postorder_left_tree_idx, left_tree_count)
            node.right = build_helper(preorder_left_idx + left_tree_count + 1, preorder_right_idx, postorder_left_tree_idx + 1, postorder_right_idx - 1, right_tree_count)
            return node

        return build_helper(0, n - 1, 0, n - 1, n)

# time O(n)
# space O(n)
# using tree and divide and conquer and re-build tree (top-down)
'''
1. preorder = Root + [Left Subtree] + Right Subtree
            = Root + [Left Subtree Root + Rest of Left Subtree] + Right Subtree
2. postorder = [Left Subtree] + Right Subtree + Root
             = [Rest of Left Subtree + Left Subtree Root] + Right Subtree + Root
'''