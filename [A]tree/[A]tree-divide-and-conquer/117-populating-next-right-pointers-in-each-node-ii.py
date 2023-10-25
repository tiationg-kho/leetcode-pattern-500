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
        upper_level_start = root
        while upper_level_start:
            upper_level_cur = upper_level_start
            lower_level_start = None
            lower_level_cur_end = None
            while upper_level_cur:
                if upper_level_cur.left:
                    if not lower_level_start:
                        lower_level_start = upper_level_cur.left
                        lower_level_cur_end = upper_level_cur.left
                    elif lower_level_cur_end:
                        lower_level_cur_end.next = upper_level_cur.left
                        lower_level_cur_end = lower_level_cur_end.next

                if upper_level_cur.right:
                    if not lower_level_start:
                        lower_level_start = upper_level_cur.right
                        lower_level_cur_end = upper_level_cur.right
                    elif lower_level_cur_end:
                        lower_level_cur_end.next = upper_level_cur.right
                        lower_level_cur_end = lower_level_cur_end.next
                upper_level_cur = upper_level_cur.next
            upper_level_start = lower_level_start
        return root
                    
# time O(n)
# space O(1)
# using tree and divide and conquer and populate next ptr and multi pointers