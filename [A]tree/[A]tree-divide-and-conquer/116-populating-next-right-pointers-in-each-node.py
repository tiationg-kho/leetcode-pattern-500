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
        upper_level_start = root
        while upper_level_start:
            cur = upper_level_start
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            upper_level_start = upper_level_start.left
        return root
    
# time O(n)
# space O(1)
# using tree and divide and conquer and populate next ptr
# next ptr's two type: belong to same parent or belong to parents next to each other