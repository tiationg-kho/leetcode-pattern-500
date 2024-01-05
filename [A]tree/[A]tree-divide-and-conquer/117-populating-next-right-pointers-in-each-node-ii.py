"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        upper_start = root
        while upper_start:
            upper_cur = upper_start
            lower_start = None
            lower_end = None
            while upper_cur:
                if not lower_start:
                    lower_start = upper_cur.left or upper_cur.right
                if upper_cur.left:
                    if lower_end:
                        lower_end.next = upper_cur.left
                    lower_end = upper_cur.left
                if upper_cur.right:
                    if lower_end:
                        lower_end.next = upper_cur.right
                    lower_end = upper_cur.right
                upper_cur = upper_cur.next
            upper_start = lower_start
        return root

# time O(n)
# space O(1)
# using tree and divide and conquer and populate next ptr and multi pointers