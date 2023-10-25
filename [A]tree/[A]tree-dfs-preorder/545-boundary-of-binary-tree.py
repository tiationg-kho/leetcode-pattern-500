# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        root_list = []
        left_list = []
        leaf_list = []
        right_list = []

        def preorder(node, flag):
            if not node:
                return
            elif not node.left and not node.right:
                leaf_list.append(node.val)
            elif flag == 0:
                root_list.append(node.val)
                preorder(node.left, 1)
                preorder(node.right, 2)
            elif flag == 1:
                left_list.append(node.val)
                preorder(node.left, 1)
                preorder(node.right, 1 if not node.left else 3)
            elif flag == 2:
                right_list.append(node.val)
                preorder(node.left, 2 if not node.right else 3)
                preorder(node.right, 2)
            else:
                preorder(node.left, 3)
                preorder(node.right, 3)

        preorder(root, 0)
        return root_list + left_list + leaf_list + right_list[::- 1]

# time O(n)
# space O(n)
# using tree and dfs (preorder and recursive) and record leaves
'''
flag
0 is root
1 is left boundary
2 is right boundary
3 is others
'''