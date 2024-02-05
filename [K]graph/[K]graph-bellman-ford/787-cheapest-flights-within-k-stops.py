class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        node_dist = [float('inf') for _ in range(n)]
        node_dist[src] = 0

        for i in range(k + 1):
            temp_node_dist = node_dist[:]
            for p, q, w in flights:
                if node_dist[p] != float('inf') and node_dist[p] + w < temp_node_dist[q]:
                    temp_node_dist[q] = node_dist[p] + w
            node_dist = temp_node_dist
        return node_dist[dst] if node_dist[dst] != float('inf') else - 1

# time O(kE), at most O(VE) for original bellman ford algo
# space O(V)
# using graph and bellman ford and shortest path

from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for p, q, w in flights:
            graph[p].append((q, w))
        step_total = k + 1
        step_node_dist = [[float('inf') for _ in range(n)] for _ in range(step_total + 1)]
        step_node_dist[0][src] = 0
        heap = [(0, 0, src)]
        heapify(heap)
        visited = set()
        while heap:
            prev, step, node = heappop(heap)
            if node == dst:
                break
            if step == step_total:
                continue
            if (step, node) in visited:
                continue
            visited.add((step, node))
            for neighbor, w in graph[node]:
                d = prev + w
                if d < step_node_dist[step + 1][neighbor]:
                    heappush(heap, (d, step + 1, neighbor))
                    step_node_dist[step + 1][neighbor] = d

        res = float('inf')
        for s in range(step_total + 1):
            res = min(res, step_node_dist[s][dst])
        return res if res != float('inf') else - 1

# time O(Eklog(Ek))
# space O(Vk)
# using graph and dijkstra and shortest path