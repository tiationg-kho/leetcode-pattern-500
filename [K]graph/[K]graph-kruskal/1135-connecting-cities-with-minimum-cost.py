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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x: x[2])
        uf = UnionFind(n)
        mst = []
        res = 0
        for p, q, w in connections:
            p -= 1
            q -= 1
            if not uf.is_connected(p, q):
                uf.union(p, q)
                mst.append((p, q, w))
                res += w
        return res if len(mst) == n - 1 else - 1

# time O(ElogE)
# space O(E + V)
# using graph and kruskal and mst and union find