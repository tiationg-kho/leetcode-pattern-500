from heapq import *
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegrees = [0 for _ in range(n)]
        for p, q in relations:
            p -= 1
            q -= 1
            graph[p].append(q)
            indegrees[q] += 1

        heap = []
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                heappush(heap, (time[i], i))
        
        while heap:
            prev, node = heappop(heap)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    heappush(heap, (prev + time[neighbor], neighbor))
        return prev

# time O(VlogV)
# space O(V+E)
# using graph and kahn and topological sort and heap

from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegrees = [0 for _ in range(n)]
        for p, q in relations:
            p -= 1
            q -= 1
            graph[p].append(q)
            indegrees[q] += 1

        costs = [0 for _ in range(n)]
        queue = deque([])
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
                costs[i] = time[i]
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                costs[neighbor] = max(costs[neighbor], costs[node] + time[neighbor])
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        return max(costs)
    
# time O(V+E)
# space O(V+E)
# using graph and kahn and topological sort and dp