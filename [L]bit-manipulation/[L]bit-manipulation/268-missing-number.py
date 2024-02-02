class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums) + 1):
            res ^= i
        for num in nums:
            res ^= num
        return res
    
# time O(n)
# space O(1)
# using bit manipulation and xor