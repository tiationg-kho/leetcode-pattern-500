class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows // 2):
            for c in range(cols):
                matrix[r][c], matrix[rows - 1 - r][c] = matrix[rows - 1 - r][c], matrix[r][c]
        
        for r in range(rows):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

# time O(RC)
# space O(1)
# using graph and matrix
'''
1. flip by horizontal first, then flip by main diagonal
'''