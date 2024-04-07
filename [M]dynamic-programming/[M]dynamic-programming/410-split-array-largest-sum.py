class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total
        
        dp = [[float('inf') for _ in range(k + 1)] for _ in range(n)]
        for end in range(n):
            dp[end][1] = prefix[end + 1] - prefix[0]

        for end in range(n):
            for interval in range(2, k + 1):
                for cut in range(end, interval - 2, - 1):
                    largest_sum = max(dp[cut - 1][interval - 1], prefix[end + 1] - prefix[cut])
                    dp[end][interval] = min(dp[end][interval], largest_sum)
        return dp[n - 1][k]

# time O(n**2 * k)
# space O(nk)
# using dynamic programming and interval (start from one interval)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def valid(bound):
            group = 1
            total = 0
            for num in nums:
                if num > bound:
                    return False
                if total + num > bound:
                    group += 1
                    total = num
                else:
                    total += num
            return group <= k

        left, right, boundary = 0, sum(nums), - 1
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