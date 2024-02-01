from collections import deque
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    queue = deque([(r, c)])
                    path = []
                    while queue:
                        row, col = queue.popleft()
                        path.append((row - r, col - c))
                        for next_r, next_c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                            if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or grid[next_r][next_c] == 0:
                                continue
                            queue.append((next_r, next_c))
                            visited.add((next_r, next_c))
                    islands.add(tuple(path))
        return len(islands)
    
# time O(RC)
# space O(RC)
# using graph and bfs with single source