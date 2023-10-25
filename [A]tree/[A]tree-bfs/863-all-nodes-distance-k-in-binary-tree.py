# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_parent = {root: None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
                    node_parent[child] = node
        
        res = []
        queue = deque([(target, 0)])
        visited = {target.val}
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                res.append(node.val)
            else:
                for next_node in [node.left, node.right, node_parent[node]]:
                    if next_node and next_node.val not in visited:
                        queue.append((next_node, distance + 1))
                        visited.add(next_node.val)
        return res
    
# time O(n)
# space O(n)
# using tree and bfs and build child_parent hashmap