# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            level_count = len(queue)
            cur_level = []
            for _ in range(level_count):
                node = queue.popleft()
                cur_level.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            if len(res) % 2 == 0:
                res.append(cur_level)
            else:
                res.append(cur_level[:: - 1])
        return res
    
# time O(n), due to traverse
# space O(n), due to queue's size (tree diameter or last level)
# using tree and bfs