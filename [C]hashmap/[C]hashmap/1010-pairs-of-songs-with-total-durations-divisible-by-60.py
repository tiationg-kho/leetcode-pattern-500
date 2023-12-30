from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        val_freq = defaultdict(int)
        for t in time:
            target = (60 - (t % 60)) % 60
            res += val_freq[target]
            val_freq[t % 60] += 1
        return res
        
# time O(n), due to traverse
# space O(1)
# using hashmap