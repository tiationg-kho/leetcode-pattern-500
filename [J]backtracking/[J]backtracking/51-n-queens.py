class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        g = [['.' for _ in range(n)] for _ in range(n)]
        col_set = set()
        diag_set = set()
        antidiag_set = set()
        res = []

        def dfs(r):
            if r == n:
                puzzle = []
                for row in range(len(g)):
                    puzzle.append(''.join(g[row]))
                res.append(puzzle)
                return
            for c in range(n):
                if c in col_set or r - c in diag_set or r + c in antidiag_set:
                    continue
                col_set.add(c)
                diag_set.add(r - c)
                antidiag_set.add(r + c)
                g[r][c] = 'Q'
                dfs(r + 1)
                col_set.remove(c)
                diag_set.remove(r - c)
                antidiag_set.remove(r + c)
                g[r][c] = '.'
        
        dfs(0)
        return res
    
# time O(n!)
# space O(n**2), not counting output
# using dfs and backtracking and backtracking with constraints