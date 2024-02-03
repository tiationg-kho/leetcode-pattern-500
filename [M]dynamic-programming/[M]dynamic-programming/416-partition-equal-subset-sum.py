class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for num in nums:
            for total in range(target, num - 1, - 1):
                dp[total] = dp[total] or dp[total - num]
        return dp[target]

# time O(nm), n is the number of nums
# space O(m), m is the sum of all elements in nums
# using dynamic programming and knapsack (0-1 knapsack) 