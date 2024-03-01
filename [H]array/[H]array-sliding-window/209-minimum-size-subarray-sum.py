class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res != float('inf') else 0

# time O(n)
# space O(1)
# using array and shrink type sliding window
'''
1. notice: only works for positive elements
2. if num can be negative then use monotonic queue and prefix sum and sliding window
3. think about [20, -30, 20, 10] and 30, correct res should be 2
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        def valid(length):
            total = 0
            for i in range(len(nums)):
                total += nums[i]
                if i >= length:
                    total -= nums[i - length]
                if total >= target:
                    return True
            return False
        
        left, right, boundary = 1, len(nums), 0
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary
    
# time O(nlogn)
# space O(1)
# using binary search and search in sth’s range
'''
1. notice: only works for positive elements
2. if num can be negative then use monotonic queue and prefix sum and sliding window
3. think about [-10, -10, -10, 20] and 20, correct res should be 1
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total
        
        res = float('inf')
        mono_queue = deque([])
        for i in range(len(prefix)):
            while mono_queue and prefix[i] - prefix[mono_queue[0]] >= target:
                idx = mono_queue.popleft()
                res = min(res, i - idx)
            while mono_queue and prefix[i] <= prefix[mono_queue[- 1]]:
                mono_queue.pop()
            mono_queue.append(i)
        return res if res != float('inf') else 0

# time O(n)
# space O(n)
# using monotonic queue and prefix sum and sliding window