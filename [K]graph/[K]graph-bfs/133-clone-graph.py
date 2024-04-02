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
            return node
        old_new = {}
        queue = deque([])
        visited = set()
        queue.append(node)
        visited.add(node)
        while queue:
            old_node = queue.popleft()
            if old_node not in old_new:
                old_new[old_node] = Node(old_node.val)
            for neighbor in old_node.neighbors:
                if neighbor not in old_new:
                    old_new[neighbor] = Node(neighbor.val)
                old_new[old_node].neighbors.append(old_new[neighbor])
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return old_new[node]
    
# time O(n)
# space O(n)
# using graph and bfs with single source and hashmap