class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for r in range(rows):
            total = 0
            for c in range(cols):
                total += matrix[r][c]
                self.prefix[r + 1][c + 1] = self.prefix[r][c + 1] + total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# time O(1) for sumRegion(), O(RC) for init
# space O(RC)
# using array and prefix sum and standard prefix sum