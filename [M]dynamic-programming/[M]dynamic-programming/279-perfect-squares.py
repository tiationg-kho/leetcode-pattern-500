class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, n + 1):
            if i ** 2 <= n:
                nums.append(i ** 2)
            else:
                break
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0

        for num in nums:
            for total in range(1, n + 1):
                if total >= num:
                    dp[total] = min(dp[total], dp[total - num] + 1)
        return dp[n]
    
# time O(n**0.5 * n)
# space O(n), due to dp table
# using dynamic programming and knapsack (complete knapsack) 