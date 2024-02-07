class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur = max(prev_prev + nums[i], prev)
            prev_prev, prev = prev, cur
        return cur
        
# time O(n), due to traverse
# space O(1)
# using dynamic programming and linear sequence