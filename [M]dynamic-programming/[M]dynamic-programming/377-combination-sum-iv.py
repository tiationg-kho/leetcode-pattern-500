class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for total in range(1, target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]
        return dp[target]
        
# time O(m*n), m is the target and n is the number of nums
# space O(m), m is the target
# using dynamic programming and knapsack (permutation knapsack) 