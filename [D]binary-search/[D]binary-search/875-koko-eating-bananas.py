from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def valid(speed):
            hour = 0
            for p in piles:
                hour += ceil(p / speed)
            return hour <= h
        
        left, right, boundary = 1, sum(piles), - 1
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                right = m - 1
            else:
                left = m + 1
        return boundary
    
# time O(nlogm), n is the number of piles and m is the size of max pile 
# space O(1)
# using binary search and search in sth’s range