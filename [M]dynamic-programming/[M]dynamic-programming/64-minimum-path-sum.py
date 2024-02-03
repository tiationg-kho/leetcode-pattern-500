class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                elif r == 0:
                    dp[r][c] = dp[r][c - 1] + grid[r][c]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                else:
                    dp[r][c] = min(dp[r][c - 1], dp[r - 1][c]) + grid[r][c]
                    
        return dp[rows - 1][cols - 1]

# time O(RC)
# space O(RC)
# using dynamic programming and 2D