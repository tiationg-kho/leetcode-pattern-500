# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 1
        while queue:
            level_count = len(queue)
            cur_level = []
            for _ in range(level_count):
                node = queue.popleft()
                if level % 2 == 0:
                    cur_level.append(node)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

            left, right = 0, len(cur_level) - 1
            while left < right:
                cur_level[left].val, cur_level[right].val = cur_level[right].val, cur_level[left].val
                left += 1
                right -= 1
                
            level += 1

        return root
    
# time O(n)
# space O(n)
# using tree and bfs and two pointers