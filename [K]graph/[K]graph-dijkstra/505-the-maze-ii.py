from heapq import *
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dist[start[0]][start[1]] = 0
        heap = [(0, start[0], start[1])]
        heapify(heap)
        visited = set()
        while heap:
            prev, r, c = heappop(heap)
            if (r, c) == (destination[0], destination[1]):
                return prev
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for offset_r, offset_c in [(1, 0), (0, 1), (- 1, 0), (0, - 1)]:
                next_r, next_c = r, c
                w = 0
                while next_r + offset_r in range(rows) and next_c + offset_c in range(cols) and maze[next_r + offset_r][next_c + offset_c] != 1:
                    next_r += offset_r
                    next_c += offset_c
                    w += 1
                d = prev + w
                if d < dist[next_r][next_c]:
                    heappush(heap, (d, next_r, next_c))
                    dist[next_r][next_c] = d
        return - 1

# time O(V + ElogE), V is RC, E is 4RC
# space O(V+E)
# using graph and dijkstra and shortest path