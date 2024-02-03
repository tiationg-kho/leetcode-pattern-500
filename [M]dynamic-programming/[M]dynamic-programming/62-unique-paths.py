class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            res[i][0] = 1
        for i in range(n):
            res[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i - 1][j] + res[i][j - 1]
                
        return res[m - 1][n - 1]
    
# time O(nm), due to grids' size
# space O(nm), due to list
# using dynamic programming and 2D