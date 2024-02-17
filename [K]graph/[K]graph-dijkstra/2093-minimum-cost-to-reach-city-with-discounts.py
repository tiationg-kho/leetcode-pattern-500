from heapq import *
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        for p, q, w in highways:
            graph[p].append((q, w))
            graph[q].append((p, w))
        dist = [[float('inf') for _ in range(discounts + 1)] for _ in range(n)]
        dist[0][discounts] = 0
        heap = [(0, discounts, 0)]
        heapify(heap)
        visited = set()
        while heap:
            prev, discount, node = heappop(heap)
            if node == n - 1:
                return prev
            if (node, discount) in visited:
                continue
            visited.add((node, discount))
            for neighbor, w in graph[node]:
                if neighbor == node:
                    continue
                d = prev + w
                if d < dist[neighbor][discount]:
                    heappush(heap, (d, discount, neighbor))
                    dist[neighbor][discount] = d
                if discount > 0:
                    d = prev + w // 2
                    new_discount = discount - 1
                    if d < dist[neighbor][new_discount]:
                        heappush(heap, (d, new_discount, neighbor))
                        dist[neighbor][new_discount] = d

        return - 1
    
# time O(V + E + Vk + Eklog(Ek))
# space O(V+E+Vk)
# using graph and dijkstra and shortest path