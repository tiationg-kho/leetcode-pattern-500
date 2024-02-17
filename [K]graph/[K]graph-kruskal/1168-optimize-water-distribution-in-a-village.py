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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        edges = []
        for i, w in enumerate(wells):
            edges.append((w, i, n))
        for p, q, w in pipes:
            edges.append((w, p - 1, q - 1))
        edges.sort()

        res = 0
        for w, p, q in edges:
            if not uf.is_connected(p, q):
                uf.union(p, q)
                res += w
        return res
    
# time O(ElogE)
# space O(V + E)
# using graph and kruskal and mst and union find