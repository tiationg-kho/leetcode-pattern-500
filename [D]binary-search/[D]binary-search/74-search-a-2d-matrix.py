class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        def get_num(idx):
            r, c = divmod(idx, cols)
            return matrix[r][c]

        left, right, boundary = 0, rows * cols - 1, - 1
        while left <= right:
            m = (left + right) // 2
            num = get_num(m)
            if num == target:
                boundary = m
                break
            elif num > target:
                right = m - 1
            else:
                left = m + 1
        return boundary != - 1
    
# time O(log(mn))
# space O(1)
# using binary search and search in a sorted array for specific val