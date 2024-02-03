class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) % 2:
            return 0
        val = (sum(nums) + target) // 2
        if val < 0:
            return 0
        dp = [0 for _ in range(val + 1)]
        dp[0] = 1

        for num in nums:
            for total in range(val, num - 1, - 1):
                dp[total] += dp[total - num]
        return dp[val]

# time O(nV)
# space O(V)
# using dynamic programming and knapsack (0-1 knapsack) 
'''
T = V - (sum - V)
(T + sum) // 2 = V
'''