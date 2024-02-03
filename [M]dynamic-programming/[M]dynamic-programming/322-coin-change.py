class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for total in range(1, amount + 1):
                if total >= coin:
                    dp[total] = min(dp[total], dp[total - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else - 1

# time O(m * n), m is the amount and n is the number of coins
# space O(m), due to the dp list's size
# using dynamic programming and knapsack (complete knapsack) 