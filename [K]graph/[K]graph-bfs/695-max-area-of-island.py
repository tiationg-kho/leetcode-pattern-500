from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                area = 1
                queue = deque([(r, c)])
                visited.add((r, c))
                while queue:
                    row, col = queue.popleft()
                    for next_r, next_c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                        if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or grid[next_r][next_c] == 0:
                            continue
                        queue.append((next_r, next_c))
                        visited.add((next_r, next_c))
                        area += 1
                res = max(res, area)
        return res
    
# time O(RC)
# space O(RC)
# using graph and bfs with single source