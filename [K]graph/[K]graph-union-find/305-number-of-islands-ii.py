class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        elif self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        rows, cols = m, n
        n = m * n
        g = [[0 for _ in range(cols)] for _ in range(rows)]

        def get_idx(r, c):
            return r * cols + c

        uf = UnionFind(n)
        count = 0
        res = []
        for r, c in positions:
            if g[r][c] == 0:
                g[r][c] = 1
                count += 1
                for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if next_r not in range(rows) or next_c not in range(cols) or g[next_r][next_c] == 0:
                        continue
                    if not uf.is_connected(get_idx(r, c), get_idx(next_r, next_c)):
                        uf.union(get_idx(r, c), get_idx(next_r, next_c))
                        count -= 1
            res.append(count)
        return res
    
# time O(RC + n)
# space O(RC), not counting output
# using graph and union find