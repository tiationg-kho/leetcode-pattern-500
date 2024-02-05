from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)
        V = n
        time = 0
        ids = [- 1 for _ in range(V)]
        low = [- 1 for _ in range(V)]
        on_stack = [False for _ in range(V)]
        stack = []
        used_edges = set()
        res = []

        def dfs(node):
            nonlocal time
            ids[node] = time
            low[node] = time
            time += 1
            on_stack[node] = True
            stack.append(node)

            for neighbor in graph[node]:
                if (node, neighbor) in used_edges or (neighbor, node) in used_edges:
                    continue
                used_edges.add((node, neighbor))
                used_edges.add((neighbor, node))

                if ids[neighbor] == - 1:
                    dfs(neighbor)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > ids[node]:
                        res.append([node, neighbor])

                elif on_stack[neighbor]:
                    low[node] = min(low[node], ids[neighbor])

            if low[node] == ids[node]:
                component = []
                while stack:
                    stack_node = stack.pop()
                    on_stack[stack_node] = False
                    component.append(stack_node)
                    if stack_node == node:
                        break
    
        for i in range(V):
            if ids[i] == - 1:
                dfs(i)

        return res
    
# time O(V+E)
# space O(V+E)
# using graph and tarjan and scc