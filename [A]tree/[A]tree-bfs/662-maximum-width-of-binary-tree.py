# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([(root, 1)])
        while queue:
            level_count = len(queue)
            cur_level = []
            for _ in range(level_count):
                node, idx = queue.popleft()
                cur_level.append(idx)
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
            res = max(res, cur_level[- 1] - cur_level[0] + 1)
        return res
                        
# time O(n)
# space O(n), due to queue
# using tree and bfs and assign idx