class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums) - 1, - 1, - 1):
            step = 0
            while stack and nums[stack[- 1][0]] < nums[i]:
                _, step_cost = stack.pop()
                step = max(step + 1, step_cost)
            stack.append((i, step))
            res = max(res, step)
        return res
    
# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic stack (consider one side’s relationship)