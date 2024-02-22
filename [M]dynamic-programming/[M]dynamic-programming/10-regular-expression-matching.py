class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        if s[i - 1] == p[j - 2]:
                            dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                        else:
                            dp[i][j] = dp[i][j - 2]
                elif p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    pass
        
        return dp[m][n]
    
# time O(mn)
# space O(mn)
# using dynamic programming and double sequence