class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        reach = 0
        for i, num in enumerate(nums):
            reach = max(reach, i + num)
            if i == len(nums) - 1:
                return res
            if i == cur:
                res += 1
                cur = reach
        return res
                
# time O(n)
# space O(1)
# using greedy