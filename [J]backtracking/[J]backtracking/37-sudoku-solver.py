class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def valid(row, col, digit):
            for r in range(rows):
                if board[r][col] == digit:
                    return False
            for c in range(cols):
                if board[row][c] == digit:
                    return False
            for r in range(row // 3 * 3, row // 3 * 3 + 3):
                for c in range(col // 3 * 3, col // 3 * 3 + 3):
                    if board[r][c] == digit:
                        return False
            return True

        def dfs(row, col):
            if row == rows:
                return True
            if col == cols:
                return dfs(row + 1, 0)
            if board[row][col] != '.':
                return dfs(row, col + 1)
            for i in range(1, 10):
                if valid(row, col, str(i)):
                    board[row][col] = str(i)
                    if dfs(row, col + 1):
                        return True
                    board[row][col] = '.'
            return False

        dfs(0, 0)
                    
# time O(9**(nm))
# space O(nm)
# using dfs and backtracking and backtracking with constraints