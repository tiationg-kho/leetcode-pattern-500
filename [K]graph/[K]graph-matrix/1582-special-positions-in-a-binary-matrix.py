class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row = [0 for _ in range(rows)]
        col = [0 for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    row[r] += 1
                    col[c] += 1
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and row[r] == 1 and col[c] == 1:
                    res += 1
        return res
      
# time O(RC)
# space O(R+C)
# using graph and matrix