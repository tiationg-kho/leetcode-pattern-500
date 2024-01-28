from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque([])
        for right, num in enumerate(nums):
            left = right - k + 1
            while queue and nums[queue[- 1]] <= num:
                queue.pop()
            queue.append(right)
            while queue and queue[0] < left:
                queue.popleft()
            if left >= 0:
                res.append(nums[queue[0]])
        return res
    
# time O(n)
# space O(k)
# using stack and queue and montonic and monotonic queue and sliding window