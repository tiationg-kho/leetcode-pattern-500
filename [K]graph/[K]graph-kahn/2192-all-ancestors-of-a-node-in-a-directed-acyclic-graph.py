from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegrees = [0 for _ in range(n)]
        for p, q in edges:
            graph[p].append(q)
            indegrees[q] += 1
        queue = deque([])
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)

        dag = []
        res = [set() for _ in range(n)]
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                res[neighbor].update(res[node])
                res[neighbor].add(node)

        return [sorted(list(ancestors)) for ancestors in res]

# time O(V + VE + V*VlogV)
# space O(V + E + V**2)
# using graph and kahn and topological sort and sort