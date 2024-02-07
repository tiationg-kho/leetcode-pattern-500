class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(left, right):
            n = right - left + 1
            if n == 1:
                return nums[left]
            if n == 2:
                return max(nums[left], nums[left + 1])
            prev_prev = nums[left]
            prev = max(nums[left], nums[left + 1])
            for i in range(left + 2, right + 1):
                cur = max(prev_prev + nums[i], prev)
                prev_prev, prev = prev, cur
            return cur

        if len(nums) == 1:
            return nums[0]
        return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))

# time O(n), due to traverse twice
# space O(1)
# using dynamic programming and linear sequence