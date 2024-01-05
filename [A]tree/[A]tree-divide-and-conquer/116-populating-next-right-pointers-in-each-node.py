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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        upper_start = root
        while upper_start:
            upper_cur = upper_start
            while upper_cur:
                if upper_cur.left:
                    upper_cur.left.next = upper_cur.right
                if upper_cur.right and upper_cur.next:
                    upper_cur.right.next = upper_cur.next.left
                upper_cur = upper_cur.next
            upper_start = upper_start.left
        return root
    
# time O(n)
# space O(1)
# using tree and divide and conquer and populate next ptr
# next ptr's two type: belong to same parent or belong to parents next to each other