class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        dp[row][column][0] = 1

        for step in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    prob = 0
                    for offset_r, offset_c in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
                        if r + offset_r not in range(n) or c + offset_c not in range(n):
                            continue
                        prob += dp[r + offset_r][c + offset_c][step - 1]
                    prob /= 8
                    dp[r][c][step] = prob
                    
        res = 0
        for r in range(n):
            for c in range(n):
                res += dp[r][c][k]
        return res
    
# time O(RCK)
# space O(RCK)
# using dynamic programming and 2D