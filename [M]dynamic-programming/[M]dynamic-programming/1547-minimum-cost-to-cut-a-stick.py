class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[float('inf') for _ in range(m)] for _ in range(m)]
        for i in range(m - 1):
            dp[i][i + 1] = 0
 
        for length in range(2, m):
            for start in range(m):
                end = start + length
                if end >= m:
                    break
                for cut in range(start + 1, end):
                    cost = cuts[end] - cuts[start]
                    dp[start][end] = min(dp[start][end], dp[start][cut] + cost + dp[cut][end])

        return dp[0][m - 1]

# time O(m**3)
# space O(m**2)
# using dynamic programming and interval (start from short interval)