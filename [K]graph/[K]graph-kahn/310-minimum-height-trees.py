from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        indegrees = [0 for _ in range(n)]
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
            indegrees[q] += 1
            indegrees[p] += 1

        queue = deque([])
        for i, indegree in enumerate(indegrees):
            if indegree == 1:
                queue.append(i)

        while queue:
            count = len(queue)
            level_nodes = []
            for _ in range(count):
                node = queue.popleft()
                level_nodes.append(node)
                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 1:
                        queue.append(neighbor)
        return level_nodes
    
# time O(V+E)
# space O(V+E), due to building graph
# using graph and kahn and topological sort
'''
1. we want the root node as center as possible
2. so start from removing all cur leaf nodes in each round
'''