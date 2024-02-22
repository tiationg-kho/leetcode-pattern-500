class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)
        if n == k:
            return 0

        count = [[0 for _ in range(n)] for _ in range(n)]
        for length in range(2, n + 1):
            for start in range(n):
                end = start + length - 1
                if end >= n:
                    break
                if s[start] == s[end]:
                    count[start][end] = count[start + 1][end - 1] if start + 1 <= end - 1 else 0
                else:
                    count[start][end] = count[start + 1][end - 1] + 1 if start + 1 <= end - 1 else 1

        dp = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = count[0][i]

        for end in range(n):
            for interval in range(2, k + 1):
                for cut in range(end, interval - 2, - 1):
                    dp[end][interval] = min(dp[end][interval], dp[cut - 1][interval - 1] + count[cut][end])

        return dp[n - 1][k]

# time O(n**2 + n**2 * k)
# space O(n**2 + nk)
# using dynamic programming and interval (start from one interval) and interval (start from short interval)