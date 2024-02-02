class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
    
# time O(n)
# space O(1)
# using bit manipulation and xor