class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        res = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "0":
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                res = max(res, dp[i][j] ** 2)
        return res
    
# time O(nm), due to matrix' size
# space O(nm), due to list
# using dynamic programming and 2D