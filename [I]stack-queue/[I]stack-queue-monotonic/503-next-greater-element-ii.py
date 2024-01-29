class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [- 1 for _ in range(len(nums))]
        stack = []
        for i in range(2 * len(nums)):
            j = i % len(nums)
            while stack and nums[stack[- 1]] < nums[j]:
                idx = stack.pop()
                res[idx] = nums[j]
            if i < len(nums):
                stack.append(i)
        return res

# time O(n), each num will only pop and push once and both cost O(1)
# space O(n), due to deque's size
# using stack and queue and montonic and monotonic stack (consider one side’s relationship)