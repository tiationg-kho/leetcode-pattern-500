class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, jump in enumerate(nums):
            if far < i:
                return False
            far = max(far, i + jump)
        return True

# time O(n)
# space O(1)
# using dynamic programming and linear sequence