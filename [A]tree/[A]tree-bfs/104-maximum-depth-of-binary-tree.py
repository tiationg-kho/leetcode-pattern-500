# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            for child in [node.left, node.right]:
                if child:
                    queue.append((child, level + 1))
        return level
    
# time O(n), due to bfs
# space O(n), due to queue's size, it can be n/2 in a balanced tree's deepest level
# using tree and bfs