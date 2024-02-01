from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        if grid[0][0] == 0:
            queue.append((0, 0, 1))
            visited.add((0, 0))
        while queue:
            r, c, count = queue.popleft()
            if (r, c) == (rows - 1, cols - 1):
                return count
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or grid[next_r][next_c] == 1:
                    continue
                queue.append((next_r, next_c, count + 1))
                visited.add((next_r, next_c))
        return - 1
    
# time O(RC)
# space O(RC)
# using graph and bfs with single source