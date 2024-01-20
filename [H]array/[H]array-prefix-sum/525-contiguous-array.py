class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [- 1 if num == 0 else 1 for num in nums]

        prefix_idx = {}
        prefix_idx[0] = - 1
        total = 0
        res = 0
        for i, num in enumerate(nums):
            total += num
            if total in prefix_idx:
                res = max(res, i - prefix_idx[total])
            else:
                prefix_idx[total] = i
        return res

# time O(n)
# space O(n)
# using array and prefix sum and hashmap to validate the gap subarray
'''
1. if meet the same prefix in hashmap means the gap is balanced
'''