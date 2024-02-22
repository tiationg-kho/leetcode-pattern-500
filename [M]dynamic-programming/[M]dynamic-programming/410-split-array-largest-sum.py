class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = prefix[i + 1] - prefix[0]
        
        for end in range(n):
            for interval in range(2, k + 1):
                for cut in range(end, interval - 2, - 1):
                    cur_res = max(dp[cut - 1][interval - 1], prefix[end + 1] - prefix[cut])
                    dp[end][interval] = min(dp[end][interval], cur_res)
        
        return dp[n - 1][k]

# time O(n** 2 * k)
# space O(nk)
# using dynamic programming and interval (start from one interval)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def valid(limit):
            total = 0
            group = 0
            for num in nums:
                if num > limit:
                    return False
                if total + num <= limit:
                    total += num
                else:
                    group += 1
                    total = num
            if total:
                group += 1
            return group <= k

        total = sum(nums)
        left, right, boundary = 0, total, - 1
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary

# time O(nlogm), m is the total of nums
# space O(1)
# using binary search and search in sth’s range