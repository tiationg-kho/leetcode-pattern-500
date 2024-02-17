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
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def get_id(r, c):
            return r * cols + c

        nodes = []
        for r in range(rows):
            for c in range(cols):
                nodes.append((- grid[r][c], get_id(r, c), r, c))
        nodes.sort()

        n = rows * cols
        uf = UnionFind(n)
        for neg_val, idx, r, c in nodes:
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or grid[next_r][next_c] < - neg_val:
                    continue
                uf.union(idx, get_id(next_r, next_c))
            if uf.is_connected(0, n - 1):
                return - neg_val
            
# time O(RC * logRC)
# space O(RC)
# using graph and union find and sort

from heapq import *
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(- grid[0][0], 0, 0)]
        heapify(heap)
        visited = set()
        visited.add((0, 0))
        res = float('inf')
        while heap:
            neg_val, r, c = heappop(heap)
            res = min(res, - neg_val)
            if (r, c) == (rows - 1, cols - 1):
                return res
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited:
                    continue
                heappush(heap, (- grid[next_r][next_c], next_r, next_c))
                visited.add((next_r, next_c))

# time O(RC * logRC)
# space O(RC)
# using graph and bfs with single source and heap