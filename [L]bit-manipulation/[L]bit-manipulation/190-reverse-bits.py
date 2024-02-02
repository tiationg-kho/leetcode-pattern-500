class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res |= n & 1
            n >>= 1
        return res

# time O(1)
# space O(1)
# using bit manipulation and shift