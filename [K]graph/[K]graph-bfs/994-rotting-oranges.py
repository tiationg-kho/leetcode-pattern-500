from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        if fresh == 0:
            return 0

        while queue:
            r, c, minute = queue.popleft()
            if grid[r][c] == 1:
                fresh -= 1
                if fresh == 0:
                    return minute
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or grid[next_r][next_c] != 1:
                    continue
                queue.append((next_r, next_c, minute + 1))
                visited.add((next_r, next_c))
            
        return - 1
    
# time O(RC)
# space O(RC)
# using graph and bfs with multiple sources