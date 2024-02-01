from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        visited = set()
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, step = queue.popleft()
            res[r][c] = step
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited:
                    continue
                queue.append((next_r, next_c, step + 1))
                visited.add((next_r, next_c))
        return res
    
# time O(RC)
# space O(RC)
# using graph and bfs with multiple sources