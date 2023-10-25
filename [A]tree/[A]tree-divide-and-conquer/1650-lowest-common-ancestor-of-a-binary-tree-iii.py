"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr1, ptr2 = p, q
        while ptr1 != ptr2:
            if not ptr1:
                ptr1 = q
            else:
                ptr1 = ptr1.parent
            if not ptr2:
                ptr2 = p
            else:
                ptr2 = ptr2.parent

        return ptr1
        
# time O(n)
# space O(1)
# using tree and divide and conquer and find LCA and two pointers
# p→LCA + LCA→root + q→LCA is same as q→LCA + LCA→root + p→LCA