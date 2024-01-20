from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        total = 0
        res = 0
        for num in nums:
            total += num
            total %= k
            res += prefix_count[total]
            prefix_count[total] += 1
        return res
    
# time O(n), due to traverse
# space O(n)
# using array and prefix sum and hashmap to validate the gap subarray