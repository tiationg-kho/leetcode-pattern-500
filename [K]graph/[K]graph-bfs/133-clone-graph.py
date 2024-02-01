"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            old = queue.popleft()
            for old_neighbor in old.neighbors:
                if old_neighbor not in old_new:
                    old_new[old_neighbor] = Node(old_neighbor.val)
                    queue.append(old_neighbor)
                old_new[old].neighbors.append(old_new[old_neighbor])
        return old_new[node]
    
# time O(n)
# space O(n)
# using graph and bfs with single source and hashmap