class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        total = 1
        for i, num in enumerate(nums):
            res[i] = total
            total *= num
        
        total = 1
        for i in range(len(nums) - 1, - 1, - 1):
            res[i] *= total
            total *= nums[i]

        return res
    
# time O(n)
# space O(1), not counting output list
# using array and prefix sum and standard prefix sum