from collections import defaultdict
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask_freq = defaultdict(int)
        mask_freq[0] = 1
        res = 0
        mask = 0
        for c in word:
            mask ^= 1 << (ord(c) - ord('a'))
            for i in range(10):
                res += mask_freq[mask ^ (1 << i)]
            res += mask_freq[mask]
            mask_freq[mask] += 1
        return res
        
# time O(n)
# space O(min(n, 2**10))
# using bit manipulation and bitmasking and prefix sum and hashmap to validate the gap subarray