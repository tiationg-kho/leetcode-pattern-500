# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        mat = binaryMatrix
        rows, cols = mat.dimensions()
        res = - 1
        row = 0
        while row < rows:
            left = 0
            right = res - 1 if res != - 1 else cols - 1
            while left <= right:
                m = (left + right) // 2
                if mat.get(row, m) == 1:
                    res = m
                    right = m - 1
                else:
                    left = m + 1
            row += 1
        return res
        
# time O(RlogC)
# space O(1)
# using binary search and search in a sorted array for most close val