class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        val = sum(stones) // 2
        dp = [0 for _ in range(val + 1)]

        for stone in stones:
            for total in range(val, stone - 1, - 1):
                dp[total] = max(dp[total], dp[total - stone] + stone)
        
        group_a = dp[val]
        group_b = sum(stones) - group_a
        return group_b - group_a

# time O(nV), V is half of sum of stones
# space O(V)
# using dynamic programming and knapsack (0-1 knapsack) 