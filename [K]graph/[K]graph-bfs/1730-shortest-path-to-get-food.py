from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '*':
                    queue.append((r, c, 0))
        while queue:
            r, c, step = queue.popleft()
            if grid[r][c] == '#':
                return step
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or grid[next_r][next_c] == 'X':
                    continue
                queue.append((next_r, next_c, step + 1))
                visited.add((next_r, next_c))

        return - 1

# time O(RC)
# space O(RC)
# using graph and bfs with single source