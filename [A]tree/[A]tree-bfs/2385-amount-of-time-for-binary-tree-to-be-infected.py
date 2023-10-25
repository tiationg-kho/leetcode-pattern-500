# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        start_node = None
        node_parent = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == start:
                start_node = node
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
                    node_parent[child] = node
        
        queue = deque([(start_node, 0)])
        visited = {start_node.val}
        while queue:
            node, distance = queue.popleft()
            for next_node in [node.left, node.right, node_parent[node]]:
                if next_node and next_node.val not in visited:
                    queue.append((next_node, distance + 1))
                    visited.add(next_node.val)
        return distance

# time O(n)
# space O(n)
# using tree and bfs and build child_parent hashmap