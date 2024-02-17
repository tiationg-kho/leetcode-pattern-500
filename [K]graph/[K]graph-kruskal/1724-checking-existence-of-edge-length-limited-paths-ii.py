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

from collections import defaultdict
class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        self.edges = sorted(edgeList, key = lambda x: x[2])
        self.limit_parent = defaultdict(list)
        self.uf = UnionFind(n)
        for u, v, w in self.edges:
            if w not in self.limit_parent:
                self.limit_parent[w] = self.uf.parent[:]
            if not self.uf.is_connected(u, v):
                self.uf.union(u, v)
        self.limit_parent[float('inf')] = self.uf.parent[:]
        self.limits = list(self.limit_parent.keys())

    def query(self, p: int, q: int, limit: int) -> bool:
        left, right, boundary = 0, len(self.limits) - 1, - 1
        while left <= right:
            m = (left + right) // 2
            if limit == self.limits[m]:
                boundary = m
                break
            elif limit > self.limits[m]:
                boundary = m + 1
                left = m + 2
            else:
                right = m - 1
        if boundary == - 1:
            return False
        self.uf.parent = self.limit_parent[self.limits[boundary]]
        return self.uf.is_connected(p, q)

# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)

# time O(ElogE + EV) for init, O(logE) for query()
# space O(EV) for init, O(1) for query()
# using graph and kruskal and mst and union find and binary search and hashmap