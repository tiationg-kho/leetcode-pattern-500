class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_idx = {}
        prefix_idx[0] = - 1

        total = 0
        for i, num in enumerate(nums):
            total += num
            total %= k
            if total in prefix_idx and i - prefix_idx[total] >= 2:
                return True
            if total not in prefix_idx:
                prefix_idx[total] = i
        return False
    
# time O(n)
# space O(n)
# using array and prefix sum and hashmap to validate the gap subarray