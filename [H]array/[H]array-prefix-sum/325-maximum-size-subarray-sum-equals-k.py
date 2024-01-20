class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_idx = {}
        prefix_idx[0] = - 1

        total = 0
        res = 0
        for i, num in enumerate(nums):
            total += num
            if total - k in prefix_idx:
                res = max(res, i - prefix_idx[total - k])
            if total not in prefix_idx:
                prefix_idx[total] = i
        return res
    
# time O(n)
# space O(n)
# using array and prefix sum and hashmap to validate the gap subarray