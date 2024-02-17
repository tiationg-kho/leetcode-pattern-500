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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sort_edges = []
        for i, (p, q, w) in enumerate(edges):
            sort_edges.append((w, p, q, i))
        sort_edges.sort()

        def mst(exclude=None, include=None):
            uf = UnionFind(n)
            res = []
            if include != None:
                p, q, w = edges[include]
                uf.union(p, q)
                res.append(w)
            for w, p, q, i in sort_edges:
                if i == exclude or i == include:
                    continue
                if not uf.is_connected(p, q):
                    uf.union(p, q)
                    res.append(w)
            return sum(res) if len(res) == n - 1 else float('inf')

        cost = mst()
        pseudo_criticals = set()
        for i in range(len(edges)):
            if cost == mst(include=i):
                pseudo_criticals.add(i)
        criticals = []
        for i in list(pseudo_criticals):
            if cost < mst(exclude=i):
                criticals.append(i)
                pseudo_criticals.remove(i)

        return [criticals, list(pseudo_criticals)]

# time O(E**2)
# space O(V + E)
# using graph and kruskal and mst and union find