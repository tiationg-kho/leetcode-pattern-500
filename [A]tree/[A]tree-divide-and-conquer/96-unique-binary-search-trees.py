class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for total_count in range(2, n + 1):
            for left_count in range(0, total_count):
                dp[total_count] += dp[left_count] * dp[total_count - left_count - 1]
        return dp[n]
        
# time O(n**2)
# space O(n)
# using tree and divide and conquer and unique BST and dp
# dp[i] means i nodes can have how many unique binary trees
# this problem involves Catalan Number's solution which is O(n)