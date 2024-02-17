from collections import deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        indegrees = [0 for _ in range(n)]
        for p, q in relations:
            p -= 1
            q -= 1
            graph[p].append(q)
            indegrees[q] += 1
        
        queue = deque([])
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append((i, 1))

        res = []
        while queue:
            node, step = queue.popleft()
            res.append(node)
            if len(res) == n:
                return step
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append((neighbor, step + 1))
            
        return - 1

# time O(V+E)
# space O(V+E)
# using graph and kahn and topological sort