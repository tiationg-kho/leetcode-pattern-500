from collections import deque
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited or grid2[r][c] == 0:
                    continue
                queue = deque([(r, c)])
                visited.add((r, c))
                match = True
                while queue:
                    row, col = queue.popleft()
                    if grid1[row][col] == 0:
                        match = False
                    for next_r, next_c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                        if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or grid2[next_r][next_c] == 0:
                            continue
                        queue.append((next_r, next_c))
                        visited.add((next_r, next_c))
                if match:
                    res += 1
        return res
    
# time O(RC)
# space O(RC)
# using graph and bfs with single source