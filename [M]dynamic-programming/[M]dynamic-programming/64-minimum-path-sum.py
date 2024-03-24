class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
                    
        return dp[rows - 1][cols - 1]

# time O(RC)
# space O(RC)
# using dynamic programming and 2D