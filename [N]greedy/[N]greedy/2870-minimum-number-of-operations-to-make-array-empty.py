from collections import defaultdict
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        res = 0
        for num, freq in num_freq.items():
            if freq == 1:
                return - 1
            count = math.ceil(freq / 3)
            res += count
        return res

# time O(n)
# space O(n)
# using greedy and hashmap