class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_p = nums[0]
        max_p = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            min_p, max_p = min(nums[i], min_p * nums[i], max_p * nums[i]), max(nums[i], max_p * nums[i], min_p * nums[i])
            res = max(res, max_p)
        return res
    
# time O(n), due to traverse
# space O(1)
# using dynamic programming and linear sequence