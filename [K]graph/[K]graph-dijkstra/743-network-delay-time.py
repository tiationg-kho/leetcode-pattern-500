from collections import defaultdict
from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for p, q, w in times:
            graph[p - 1].append((q - 1, w))
        start = k - 1
        dist = [float('inf') for _ in range(n)]
        dist[start] = 0
        heap = [(0, start)]
        heapify(heap)
        visited = set()
        while heap:
            prev, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for neighbor, w in graph[node]:
                cur = prev + w
                if cur < dist[neighbor]:
                    heappush(heap, (cur, neighbor))
                    dist[neighbor] = cur
        return max(dist) if max(dist) != float('inf') else - 1

# time O(V + E + ElogE), ElogE -> Elog(V**2) -> ElogV
# space O(V+E)
# using graph and dijkstra and shortest path