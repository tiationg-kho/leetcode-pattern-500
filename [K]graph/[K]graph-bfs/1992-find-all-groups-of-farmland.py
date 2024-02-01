from collections import deque
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        visited = set()
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited or land[r][c] == 0:
                    continue
                queue = deque([(r, c)])
                visited.add((r, c))
                max_r, max_c = r, c
                while queue:
                    row, col = queue.popleft()
                    max_r, max_c = max(max_r, row), max(max_c, col)
                    for next_r, next_c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                        if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or land[next_r][next_c] == 0:
                            continue
                        queue.append((next_r, next_c))
                        visited.add((next_r, next_c))
                res.append([r, c, max_r, max_c])
        return res
    
# time O(RC)
# space O(RC)
# using graph and bfs with single source