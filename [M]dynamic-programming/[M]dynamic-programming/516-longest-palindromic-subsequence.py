class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for start in range(n):
                end = start + length - 1
                if end >= n:
                    break
                if s[start] == s[end]:
                    cur = 2
                    if start + 1 <= end - 1:
                        cur += dp[start + 1][end - 1]
                    dp[start][end] = cur
                else:
                    cur = 0
                    if start + 1 <= end - 1:
                        cur += max(dp[start][end - 1], dp[start + 1][end])
                    else:
                        cur += 1
                    dp[start][end] = cur
            
        return dp[0][n - 1]

# time O(n**2)
# space O(n**2)
# using dynamic programming and interval (start from short interval)