from heapq import *
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        nodes = [Node(c) for c in s]
        for i, p in enumerate(parent):
            if p == - 1:
                continue
            nodes[p].children.append(nodes[i])

        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0, None
            children_path = []
            for child in node.children:
                child_path, child_char = dfs(child)
                if child_char != node.val:
                    heappush(children_path, child_path)
                if len(children_path) > 2:
                    heappop(children_path)
            node_as_peak_path = sum(children_path) + 1 if children_path else 1
            res = max(res, node_as_peak_path)
            cur_path = max(children_path) + 1 if children_path else 1
            return cur_path, node.val

        dfs(nodes[0])
        return res
                    
# time O(n)
# space O(n)
# using tree and dfs (postorder and recursive) and heap