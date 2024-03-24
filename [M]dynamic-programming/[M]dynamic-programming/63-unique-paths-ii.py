class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        rows, cols = len(g), len(g[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if g[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows-  1][cols - 1]

# time O(RC)
# space O(RC)
# using dynamic programming and 2D