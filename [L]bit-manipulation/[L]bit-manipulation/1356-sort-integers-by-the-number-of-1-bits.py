class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def get_count(n):
            res = 0
            for _ in range(32):
                if n & 1:
                    res += 1
                n >>= 1
            return res

        return sorted(arr, key = lambda x: (get_count(x), x))

# time O(nlogn)
# space O(1), not count built in sort's cost and output list
# using bit manipulation and shift