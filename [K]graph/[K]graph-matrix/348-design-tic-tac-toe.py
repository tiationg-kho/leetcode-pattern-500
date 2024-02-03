class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0 for _ in range(n)]
        self.col = [0 for _ in range(n)]
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        weight = 1 if player == 1 else - 1
        self.row[row] += weight
        self.col[col] += weight
        if row == col:
            self.diag += weight
        if row + col == self.n - 1:
            self.anti_diag += weight
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return 1 if player == 1 else 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# time O(1)
# space O(n), due to lists
# using graph and matrix