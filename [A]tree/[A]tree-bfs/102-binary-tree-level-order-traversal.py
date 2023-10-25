# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return root
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
            res.append(cur_level)
        return res
    
# time O(n), due to traversal
# space O(n), queue can have a size of n/2 or the list's size to store nodes
# using tree and bfs