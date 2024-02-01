from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for p, q in edges:
            graph[p].append(q)
            graph[q].append(p)
        
        visited = {0}
        queue = deque([(0, - 1)])
        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                queue.append((neighbor, node))
                visited.add(neighbor)

        return len(visited) == n
    
# time O(V+E)
# space O(V+E)
# using graph and bfs with single source
'''
1. tree is a special graph with properties that
    - connected
    - acyclic
    - non-direction edges
    - one path between any two vertices/nodes
'''

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.count = n
    
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
        self.count -= 1
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def get_count(self):
        return self.count

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for p, q in edges:
            if uf.is_connected(p, q):
                return False
            uf.union(p, q)
        return uf.get_count() == 1

# time O(V+E)
# space O(V)
# using graph and union find
'''
1. tree is a special graph with properties that
    - connected
    - acyclic
    - non-direction edges
    - one path between any two vertices/nodes
'''