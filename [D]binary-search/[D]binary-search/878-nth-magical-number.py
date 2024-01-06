from math import lcm
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        
        def valid(val):
            l = lcm(a, b)
            return (val // a + val // b - val // l) >= n

        left, right, boundary = min(a, b), n * min(a, b), - 1
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary % (10**9 + 7)

# time O(log(min(a, b)*n))
# space O(1)
# using binary search and search in sth’s range