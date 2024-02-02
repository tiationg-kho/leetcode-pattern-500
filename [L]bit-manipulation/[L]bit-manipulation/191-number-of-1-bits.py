class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            if n & 1:
                res += 1
            n >>= 1
        return res
        
# time O(1), due to 32 bit int
# space O(1)
# using bit manipulation and shift