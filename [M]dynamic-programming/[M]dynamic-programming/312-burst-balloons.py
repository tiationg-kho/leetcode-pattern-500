class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i, num in enumerate(nums):
            cur = num
            if i - 1 >= 0:
                cur *= nums[i - 1]
            if i + 1 < n:
                cur *= nums[i + 1]
            dp[i][i] = cur
        
        for length in range(2, n + 1):
            for start in range(n):
                end = start + length - 1
                if end >= n:
                    break
                for cut in range(start, end + 1):
                    cur = nums[cut]
                    if start - 1 >= 0:
                        cur *= nums[start - 1]
                    if end + 1 < n:
                        cur *= nums[end + 1]
                    if cut - 1 >= start:
                        cur += dp[start][cut - 1]
                    if cut + 1 <= end:
                        cur += dp[cut + 1][end]
                    dp[start][end] = max(dp[start][end], cur)
        
        return dp[0][n - 1]
    
# time O(n**3), due to width and start pointer and balloon location's loops
# space O(n**2), due to dp table
# using dynamic programming and interval (start from short interval)