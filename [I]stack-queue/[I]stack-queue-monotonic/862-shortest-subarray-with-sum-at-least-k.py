from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total

        res = float('inf')
        queue = deque([])
        for i in range(len(prefix)):
            while queue and prefix[i] - prefix[queue[0]] >= k:
                idx = queue.popleft()
                res = min(res, i - idx)
            while queue and prefix[queue[- 1]] >= prefix[i]:
                queue.pop()
            queue.append(i)
        return res if res != float('inf') else - 1

# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic queue and sliding window and prefix
'''
1. monotonic queue store the potential subarray's head idices
2. monotonic queue needs to store the smallest prefix sum at queue's head
3. because smaller prefix gets more chance to fulfill the condition
4. once it met condition, record it, then popleft it (cur round is the best condition for shortest)
5. if cur idx's prefix sum is smaller than queue's tail, then pop from queue (using cur idx is shorter)
6. append cur idx in queue
'''