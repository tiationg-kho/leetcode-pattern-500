from collections import defaultdict
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for p, q in edges:
            graph[p].add(q)

        node_flag = defaultdict(int)
        cyclic = False
        invalid_dest = False
        
        def dfs(node):
            nonlocal cyclic, invalid_dest
            node_flag[node] = 1
            if not graph[node]:
                node_flag[node] = 2
                if node != destination:
                    invalid_dest = True
                return
            for neighbor in graph[node]:
                if node_flag[neighbor] == 0:
                    dfs(neighbor)
                elif node_flag[neighbor] == 1:
                    cyclic = True
            node_flag[node] = 2

        dfs(source)

        return not cyclic and not invalid_dest

# time O(V+E)
# space O(V+E)
# using graph and dfs and detecting cycles
'''
# 0 not visited
# 1 visiting
# 2 completed visited
'''