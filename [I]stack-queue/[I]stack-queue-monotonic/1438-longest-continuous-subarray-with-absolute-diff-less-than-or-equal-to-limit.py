from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        min_queue = deque([])
        max_queue = deque([])
        left = 0
        for right in range(len(nums)):
            while min_queue and nums[min_queue[- 1]] >= nums[right]:
                min_queue.pop()
            min_queue.append(right)
            while max_queue and nums[max_queue[- 1]] <= nums[right]:
                max_queue.pop()
            max_queue.append(right)
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                left += 1
                if min_queue[0] < left:
                    min_queue.popleft()
                if max_queue[0] < left:
                    max_queue.popleft()
            res = max(res, right - left + 1)
        return res
    
# time O(n), each num will only pop and push twice and both cost O(1)
# space O(n), due to deque's size
# using stack and queue and montonic and monotonic queue and sliding window