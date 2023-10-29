# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right, boundary = 1, n, - 1
        while left <= right:
            m = (left + right) // 2
            if isBadVersion(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary
    
# time O(logn)
# space O(1)
# using binary search and search in sth’s range