class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        two_step_before = 1
        one_step_before = 2
        for i in range(3, n + 1):
            cur = two_step_before + one_step_before
            two_step_before, one_step_before = one_step_before, cur
        return cur

# time O(n)
# space O(1)
# using dynamic programming and linear sequence