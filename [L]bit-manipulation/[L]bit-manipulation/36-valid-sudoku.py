class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        def valid(start_r, end_r, start_c, end_c):
            val = 0
            for r in range(start_r, end_r + 1):
                for c in range(start_c, end_c + 1):
                    if board[r][c] == '.':
                        continue
                    if val & (1 << int(board[r][c])):
                        return False
                    val |= (1 << int(board[r][c]))
            return True
        
        for r in range(rows):
            if not valid(r, r, 0, cols - 1):
                return False
        for c in range(cols):
            if not valid(0, rows - 1, c, c):
                return False
        for r in range(0, rows, 3):
            for c in range(0, cols, 3):
                if not valid(r, r + 2, c, c + 2):
                    return False
        return True
    
# time O(1)
# space O(1)
# using bit manipulation and bitmasking