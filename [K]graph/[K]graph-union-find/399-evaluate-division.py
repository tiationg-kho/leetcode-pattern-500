class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.weight = [1.0 for _ in range(n)]

    def find(self, p):
        if p != self.parent[p]:
            original_parent = self.parent[p]
            self.parent[p] = self.find(self.parent[p])
            self.weight[p] = self.weight[p] * self.weight[original_parent]
            p = self.parent[p]
        return p
    
    def union(self, p, q, w):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
            self.weight[root_q] = self.weight[p] * (1/w) / self.weight[q]
        elif self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
            self.weight[root_p] = self.weight[q] * w / self.weight[p]
        else:
            self.parent[root_p] = root_q
            self.weight[root_p] = self.weight[q] * w / self.weight[p]
            self.rank[root_q] += 1
        
    def get_weight(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return self.weight[p] / self.weight[q]
        return - 1.0

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        s_idx = {}
        idx = 0
        for p, q in equations:
            if p not in s_idx:
                s_idx[p] = idx
                idx += 1
            if q not in s_idx:
                s_idx[q] = idx
                idx += 1
        uf = UnionFind(idx)
        for i in range(len(equations)):
            p, q = equations[i]
            w = values[i]
            uf.union(s_idx[p], s_idx[q], w)

        res = []
        for p, q in queries:
            if p not in s_idx or q not in s_idx:
                res.append(- 1.0)
            else:
                res.append(uf.get_weight(s_idx[p], s_idx[q]))
        
        return res
            
# time O((n+m)), n is the number of equations, m is the number of queries
# space O(n), due to union find
# using graph and union find
'''
1. if A/B = 2, we record weight of node A is 2, weight of node B is 1
2. in find method, 
   we use recursive version instead of iterative because this let leaf node updates final weight relative to root node correctly
3. in find method,
   we let node connect to grand parent node instead of parent node,
   so node weight become original node weight * parent node weight
4. in union method,
   we want p connect to q. 
   if q belong to high rank tree, then update weight for root_p (q * w / p)
   if p belong to high rank tree, we treat as we want q connect to p
'''