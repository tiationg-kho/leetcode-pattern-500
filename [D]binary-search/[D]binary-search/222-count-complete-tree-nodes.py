# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        cur = root
        level = 0
        while cur:
            level += 1
            cur = cur.left

        def valid(idx):
            cur = root
            for i in range(level - 2, - 1, - 1):
                if idx & (1 << i):
                    cur = cur.right
                else:
                    cur = cur.left
            return cur != None
        
        left, right, boundary = 1 << (level - 1), (1 << level) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                left = m + 1
            else:
                right = m - 1
        return boundary
        
# time O(logn * logn)
# space O(1)
# using binary search and search in sth’s range and complete tree
'''
1. last level can have at most 2**(h-1) or 2**h - 2**(h-1) nodes
2. tree height in complete tree is logn
'''