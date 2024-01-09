from heapq import *
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        h = heightMap
        rows, cols = len(h), len(h[0])
        heap = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1) and (r, c) not in visited:
                    heappush(heap, (h[r][c], r, c))
                    visited.add((r, c))
                if (c == 0 or c == cols - 1) and (r, c) not in visited:
                    heappush(heap, (h[r][c], r, c))
                    visited.add((r, c))
        
        res = 0
        while heap:
            height, r, c = heappop(heap)
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols):
                    continue
                if (next_r, next_c) in visited:
                    continue
                res += max(height - h[next_r][next_c], 0)
                heappush(heap, (max(height, h[next_r][next_c]), next_r, next_c))
                visited.add((next_r, next_c))
        return res
        
# time O(RClog(RC)), heap size is RC
# space O(RC), due to hashset
# using heap and bfs