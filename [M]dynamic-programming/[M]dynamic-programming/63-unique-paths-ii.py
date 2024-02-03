class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        rows, cols = len(g), len(g[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        if g[0][0] == 0:
            res[0][0] = 1
        for i in range(1, rows):
            if g[i][0] == 1:
                res[i][0] = 0
            else:
                res[i][0] = res[i - 1][0]
        for i in range(1, cols):
            if g[0][i] == 1:
                res[0][i] = 0
            else:
                res[0][i] = res[0][i - 1]
        
        for i in range(1, rows):
            for j in range(1, cols):
                if g[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        
        return res[rows - 1][cols - 1]

# time O(RC)
# space O(RC)
# using dynamic programming and 2D