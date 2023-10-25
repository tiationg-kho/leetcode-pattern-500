# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def build_helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_helper(left, mid - 1)
            node.right = build_helper(mid + 1, right)
            return node

        return build_helper(0, n - 1)

# time O(n), due to traverse each node once
# space O(logn), due to memo stack's size, and output is O(n)
# using tree and divide and conquer and re-build BST (top-down approach) and binary search tree's properties