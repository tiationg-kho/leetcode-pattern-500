from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        total = 0
        res = 0
        for num in nums:
            total += num
            res += prefix_count[total - k]
            prefix_count[total] += 1
        return res
    
# time O(n)
# space O(n)
# using array and prefix sum and hashmap to validate the gap subarray
'''
1. if meet the prefix - k in hashmap means the gap is valid
'''