class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix[i + 1] = total
        
        res = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[- 1]] > nums[i]:
                idx = stack.pop()
                left_bound = stack[- 1] if stack else - 1
                right_bound = i
                res = max(res, nums[idx] * (prefix[right_bound] - prefix[left_bound + 1]))
            stack.append(i)
        while stack:
            idx = stack.pop()
            left_bound = stack[- 1] if stack else - 1
            right_bound = len(nums)
            res = max(res, nums[idx] * (prefix[right_bound] - prefix[left_bound + 1]))

        return res % (10**9+7)

# time O(n)
# space O(n), due to lists
# using stack and queue and montonic and monotonic stack (consider two side’s relationship) and prefix sum