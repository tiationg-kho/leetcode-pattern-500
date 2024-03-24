class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*' and dp[0][i - 2]:
                dp[0][i] = True
        for j in range(1, m + 1):
            dp[j][0] = False
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == '.':
                        dp[i][j] |= dp[i][j - 2]
                        dp[i][j] |= dp[i - 1][j - 2]
                        dp[i][j] |= dp[i - 1][j]
                    elif s[i - 1] == p[j - 2]:
                        dp[i][j] |= dp[i][j - 2]
                        dp[i][j] |= dp[i - 1][j - 2]
                        dp[i][j] |= dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = False

        return dp[m][n]
        
# time O(mn)
# space O(mn)
# using dynamic programming and double sequence