class Solution:
    def longestAwesome(self, s: str) -> int:
        mask_freq = {}
        mask_freq[0] = - 1
        mask = 0
        res = 0
        for i, c in enumerate(s):
            mask ^= 1 << (int(c))
            for j in range(10):
                if mask ^ (1 << j) in mask_freq:
                    res = max(res, i - mask_freq[mask ^ (1 << j)])
            if mask in mask_freq:
                res = max(res, i - mask_freq[mask])
            else:
                mask_freq[mask] = i
        return res
    
# time O(n)
# space O(min(n, 2**10))
# using bit manipulation and bitmasking and prefix sum and hashmap to validate the gap subarray