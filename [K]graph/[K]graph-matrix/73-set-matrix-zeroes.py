class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_in_first_row = False
        zero_in_first_col = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    if r == 0:
                        zero_in_first_row = True
                    if c == 0:
                        zero_in_first_col = True
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if zero_in_first_row:
            for c in range(cols):
                matrix[0][c] = 0
        if zero_in_first_col:
            for r in range(rows):
                matrix[r][0] = 0
                
# time O(RC)
# space O(1)
# using graph and matrix