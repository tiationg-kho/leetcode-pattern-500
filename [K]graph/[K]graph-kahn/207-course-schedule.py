from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        return len(res) == numCourses
    
# time O(V+E)
# space O(V+E), due to building graph
# using graph and kahn and topological sort

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for q, p in prerequisites:
            graph[p].append(q)
        
        node_flag = [0 for _ in range(numCourses)]
        cyclic = False

        def dfs(node):
            nonlocal cyclic
            node_flag[node] = 1
            for neighbor in graph[node]:
                if node_flag[neighbor] == 0:
                    dfs(neighbor)
                elif node_flag[neighbor] == 1:
                    cyclic = True
            node_flag[node] = 2

        for node in range(numCourses):
            if node_flag[node] == 0:
                dfs(node)
                
        return not cyclic

# time O(V+E)
# space O(V+E)
# using graph and dfs and detecting cycles
'''
# 0 not visited
# 1 visiting
# 2 completed visited
'''