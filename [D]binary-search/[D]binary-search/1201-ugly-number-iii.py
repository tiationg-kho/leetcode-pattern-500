from math import lcm
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        def valid(val):
            return (val // a + val // b + val // c - val // lcm(a, b) - val // lcm(b, c) - val // lcm(c, a) + val // lcm(a, b, c)) >= n

        left, right, boundary = min(a, b, c), n * min(a, b, c), - 1
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary
    
# time O(log(n * min(a, b, c))), due to the search range of binary search
# space O(1)
# using binary search and search in sth’s range