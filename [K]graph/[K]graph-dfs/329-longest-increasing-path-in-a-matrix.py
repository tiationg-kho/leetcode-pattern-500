class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cell_len = {}

        def dfs(r, c):
            total = 1
            new_total = total
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or matrix[r][c] >= matrix[next_r][next_c]:
                    continue
                if (next_r, next_c) in cell_len:
                    new_total = max(new_total, total + cell_len[(next_r, next_c)])
                else:
                    new_total = max(new_total, total + dfs(next_r, next_c))
            cell_len[(r, c)] = new_total
            return new_total

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
        return max(cell_len.values())
    
# time O(RC)
# space O(RC)
# using graph and dfs and memorizing res for long paths