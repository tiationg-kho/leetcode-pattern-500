# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right, boundary = 0, target - reader.get(0), - 1
        while left <= right:
            m = (left + right) // 2
            val = reader.get(m)
            if val == 2** 31 - 1:
                right = m - 1
            elif val > target:
                right = m - 1
            elif val == target:
                boundary = m
                break
            else:
                left = m + 1
        return boundary
    
# time O(logn)
# space O(1)
# using binary search and search in a sorted array for specific val
'''
1. notice that problem says the array contains unique elements
'''