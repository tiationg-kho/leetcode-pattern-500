from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for q, p in prerequisites:
            graph[p].append(q)
            indegrees[q] += 1

        queue = deque([])
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        return res if len(res) == numCourses else []

# time O(V+E)
# space O(V+E), due to building graph
# using graph and kahn and topological sort