# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            level_count = len(queue)
            for i in range(level_count):
                node = queue.popleft()
                if i == level_count - 1:
                    res.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
        return res
    
# time O(n), due to traverse
# space O(n), due to queue's size (tree diameter or last level)
# using tree and bfs