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
        
        p1, p2 = p, q
        while p1 != p2:
            if p1:
                p1 = p1.parent
            else:
                p1 = q
            if p2:
                p2 = p2.parent
            else:
                p2 = p
        return p1
        
# time O(n)
# space O(1)
# using tree and divide and conquer and find LCA and two pointers
# p→LCA + LCA→root + q→LCA is same as q→LCA + LCA→root + p→LCA