from collections import deque, defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
            
        queue = deque()
        for node, children in graph.items():
            if len(children) == 1:
                queue.append(node)

        while queue:
            length = len(queue)
            res = []
            for _ in range(length):
                node = queue.popleft()
                res.append(node)
                for next_node in graph[node]:
                    graph[next_node].remove(node)
                    if len(graph[next_node]) == 1:
                        queue.append(next_node)
        return res
    
# time O(V+E)
# space O(V+E), due to building graph
# using graph and kahn and topological sort
'''
1. we want the root node as center as possible
2. so start from removing all cur leaf nodes in each round
'''