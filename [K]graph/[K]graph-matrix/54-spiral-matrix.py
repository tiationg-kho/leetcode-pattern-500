class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c, d = 0, 0, 0
        res = []
        while len(res) < rows * cols:
            res.append(matrix[r][c])
            visited.add((r, c))
            next_r, next_c = r + directions[d][0], c + directions[d][1]
            if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited:
                d += 1
                d %= len(directions)
                next_r, next_c = r + directions[d][0], c + directions[d][1]
            r, c = next_r, next_c
        return res
    
# time O(RC)
# space O(RC)
# using graph and matrix and hashset