from heapq import *
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for i in range(len(edges)):
            p, q = edges[i]
            w = 1 / succProb[i]
            g[p].append((q, w))
            g[q].append((p, w))

        dist = [float('inf') for _ in range(n)]
        dist[start_node] = 1
        
        heap = [(1, start_node)]
        heapify(heap)

        visited = set()

        while heap:
            prev, node = heappop(heap)
            if node == end_node:
                return 1 / prev
            if node in visited:
                continue
            visited.add(node)
            for neighbor, w in g[node]:
                d = prev * w
                if d < dist[neighbor]:
                    heappush(heap, (d, neighbor))
                    dist[neighbor] = d
        return 0

# time O(V + E + ElogE)
# space O(V+E)
# using graph and dijkstra and shortest path