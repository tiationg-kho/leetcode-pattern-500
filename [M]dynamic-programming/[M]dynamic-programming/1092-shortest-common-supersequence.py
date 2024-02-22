class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        char = [['' for _ in range(n + 1)] for _ in range(m + 1)]
        source = [[(- 1, - 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
            char[i][0] = str1[i - 1]
            source[i][0] = (i - 1, 0)
        for j in range(1, n + 1):
            dp[0][j] = j
            char[0][j] = str2[j - 1]
            source[0][j] = (0, j - 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    char[i][j] = str1[i - 1]
                    source[i][j] = (i - 1, j - 1)
                else:
                    if dp[i][j - 1] < dp[i - 1][j]:
                        dp[i][j] = dp[i][j - 1] + 1
                        char[i][j] = str2[j - 1]
                        source[i][j] = (i, j - 1)
                    else:
                        dp[i][j] = dp[i - 1][j] + 1
                        char[i][j] = str1[i - 1]
                        source[i][j] = (i - 1, j)
        
        res = ''
        i, j = m, n
        while (i, j) != (- 1, - 1):
            res = char[i][j] + res
            i, j = source[i][j]
        return res

# time O(mn)
# space O(mn)
# using dynamic programming and double sequence