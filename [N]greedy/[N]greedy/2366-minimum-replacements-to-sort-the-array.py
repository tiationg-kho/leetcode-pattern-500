import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        res = 0
        prev = nums[- 1]
        for i in range(len(nums) - 2, - 1, - 1):
            if nums[i] > prev:
                count = math.ceil(nums[i] / prev)
                res += count - 1
                prev = math.floor(nums[i] / count)
            else:
                prev = nums[i]
        return res
      
# time O(n)
# space O(1)
# using greedy