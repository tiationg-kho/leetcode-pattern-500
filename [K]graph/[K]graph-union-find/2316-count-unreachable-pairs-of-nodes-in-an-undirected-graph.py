class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.weight = [1 for _ in range(n)]

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
            self.weight[root_p] += self.weight[root_q]
            self.weight[root_q] = 0
        elif self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
            self.weight[root_q] += self.weight[root_p]
            self.weight[root_p] = 0
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += 1
            self.weight[root_q] += self.weight[root_p]
            self.weight[root_p] = 0

    def get_weight(self, p):
        return self.weight[self.find(p)]

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for p, q in edges:
            uf.union(p, q)
        res = 0
        for i in range(n):
            res += n - uf.get_weight(i)
        return res // 2
    
# time O(V+E)
# space O(V)
# using graph and union find