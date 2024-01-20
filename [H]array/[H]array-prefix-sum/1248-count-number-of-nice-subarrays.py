from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        total = 0
        res = 0
        for num in nums:
            if num % 2:
                total += 1
            res += prefix_count[total - k]
            prefix_count[total] += 1
        return res
    
# time O(n)
# space O(n)
# using array and prefix sum and hashmap to validate the gap subarray