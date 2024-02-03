class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        res = 0
        for r in range(rows):
            for c in range(cols):
                if r == 0:
                    if matrix[r][c] == '1':
                        dp[r][c] = 1
                elif c == 0:
                    if matrix[r][c] == '1':
                        dp[r][c] = 1
                else:
                    if matrix[r][c] == '1':
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

                res = max(res, dp[r][c])
        
        return res ** 2
    
# time O(nm), due to matrix' size
# space O(nm), due to list
# using dynamic programming and 2D