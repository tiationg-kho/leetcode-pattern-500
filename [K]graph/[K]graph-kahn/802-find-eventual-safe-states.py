from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_g = [[] for _ in range(len(graph))]
        indegrees = [0 for _ in range(len(graph))]
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                rev_g[neighbor].append(node)
                indegrees[node] += 1

        queue = deque([])
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        
        res = [False for _ in range(len(graph))]
        while queue:
            node = queue.popleft()
            res[node] = True
            for neighbor in rev_g[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return [i for i, flag in enumerate(res) if flag]

# time O(V+E)
# space O(V+E)
# using graph and kahn and topological sort