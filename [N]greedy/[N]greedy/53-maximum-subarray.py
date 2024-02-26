class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        total = 0
        for num in nums:
            total += num
            res = max(res, total)
            if total < 0:
                total = 0
        return res
        
# time O(n)
# space O(1)
# using greedy