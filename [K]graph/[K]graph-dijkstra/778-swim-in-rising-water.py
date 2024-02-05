from collections import defaultdict
from heapq import *
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        node_dist = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                node_dist[(r, c)] = float('inf')
        node_dist[(0, 0)] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        heapify(heap)
        visited = set()
        while heap:
            prev, r, c = heappop(heap)
            if (r, c) == (rows - 1, cols - 1):
                break
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols):
                    continue
                d = max(prev, grid[next_r][next_c])
                if d < node_dist[(next_r, next_c)]:
                    heappush(heap, (d, next_r, next_c))
                    node_dist[(next_r, next_c)] = d

        return node_dist[(rows - 1, cols - 1)]

# time O(V + E + ElogE), V is RC, E is 4RC
# space O(V+E)
# using graph and dijkstra and shortest path