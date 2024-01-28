class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float('-inf') for _ in range(len(nums))]
        dp[0] = nums[0]

        for right in range(1, len(nums)):
            for left in range(max(0, right - k), right):
                dp[right] = max(dp[right], dp[left] + nums[right])
        return dp[- 1]

# time O(nk)
# space O(n)
# using dp (this will TLE)

from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float('-inf') for _ in range(len(nums))]
        dp[0] = nums[0]
        queue = deque([])

        for right in range(len(nums)):
            left = right - k
            while queue and queue[0] < left:
                queue.popleft()
            if queue:
                dp[right] = dp[queue[0]] + nums[right]
            while queue and dp[queue[- 1]] <= dp[right]:
                queue.pop()
            queue.append(right)

        return dp[- 1]
    
# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic queue and sliding window and dp