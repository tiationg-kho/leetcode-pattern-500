class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for total in range(1, amount + 1):
                if total >= coin:
                    dp[total] += dp[total - coin]
        return dp[amount]
    
# time O(m*n), m is the amount and n is the number of coins
# space O(m), m is the amount
# using dynamic programming and knapsack (combination knapsack) 