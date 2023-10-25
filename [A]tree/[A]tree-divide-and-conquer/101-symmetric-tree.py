# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric_helper(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if p and not q:
                return False
            if p.val != q.val:
                return False
            return symmetric_helper(p.left, q.right) and symmetric_helper(p.right, q.left)

        return symmetric_helper(root.left, root.right)
    
# time O(n), due to traverse
# space O(n), due to tree height
# using tree and divide and conquer and two branch top-down

from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
    
# time O(n)
# space O(n), due to queue and tree diameter
# using bfs (iterative)