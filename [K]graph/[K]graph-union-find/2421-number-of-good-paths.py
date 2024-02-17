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

from collections import defaultdict
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        uf = UnionFind(n)
        
        val_nodes = defaultdict(list)
        for i, val in enumerate(vals):
            val_nodes[val].append(i)
        val_edges = defaultdict(list)
        for p, q in edges:
            val_edges[vals[p]].append((p, q))
            val_edges[vals[q]].append((q, p))

        res = 0
        for val in sorted(set(vals)):
            for p, q in val_edges[val]:
                if vals[p] >= vals[q]:
                    uf.union(p, q)
            group_count = defaultdict(int)
            for node in val_nodes[val]:
                group = uf.find(node)
                group_count[group] += 1
                res += 1
            for group, count in group_count.items():
                res += (count * (count - 1)) // (2 * 1)
        return res
    
# time O(VlogV)
# space O(V+E)
# using graph and union find and sort and hashset