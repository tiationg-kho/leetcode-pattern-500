class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        counts = [[- 1 for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            next_count = 0
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or matrix[r][c] >= matrix[next_r][next_c]:
                    continue
                if counts[next_r][next_c] == - 1:
                    next_count = max(next_count, dfs(next_r, next_c))
                else:
                    next_count = max(next_count, counts[next_r][next_c])
            counts[r][c] = 1 + next_count
            return counts[r][c]
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res
    
# time O(RC)
# space O(RC)
# using graph and dfs