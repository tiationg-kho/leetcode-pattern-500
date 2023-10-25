class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right, boundary = 1, num, - 1
        while left <= right:
            m = (left + right) // 2
            if m ** 2 == num:
                boundary = m
                break
            elif m ** 2 < num:
                left = m + 1
            else:
                right = m - 1
        return boundary != - 1
    
# time O(logn)
# space O(1)
# using binary search and search in a sorted array for specific val