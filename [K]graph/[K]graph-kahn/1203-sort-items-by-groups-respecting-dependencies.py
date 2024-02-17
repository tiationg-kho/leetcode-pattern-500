from collections import deque
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def topo(graph, indegrees):
            queue = deque([])
            for i, indegree in enumerate(indegrees):
                if indegree == 0:
                    queue.append(i)
            dag = []
            while queue:
                node = queue.popleft()
                dag.append(node)
                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
            return dag

        group_id = m
        for i, g in enumerate(group):
            if g == - 1:
                group[i] = group_id
                group_id += 1
        
        group_graph = [[] for _ in range(group_id)]
        group_indegrees = [0 for _ in range(group_id)]
        item_graph = [[] for _ in range(n)]
        item_indegrees = [0 for _ in range(n)]

        for i in range(n):
            g = group[i]
            for before_item in beforeItems[i]:
                before_group = group[before_item]
                if before_group != g:
                    group_graph[before_group].append(g)
                    group_indegrees[g] += 1
                item_graph[before_item].append(i)
                item_indegrees[i] += 1
        
        group_dag = topo(group_graph, group_indegrees)
        if len(group_dag) != len(group_graph):
            return []
        item_dag = topo(item_graph, item_indegrees)
        if len(item_dag) != len(item_graph):
            return []
        
        group_items = [[] for _ in range(group_id)]
        for item in item_dag:
            g = group[item]
            group_items[g].append(item)
        res = []
        for g in group_dag:
            res.extend(group_items[g])
        return res
        
# time O(n**2 + E for groups + E for items)
# space O(n**2)
# using graph and kahn and topological sort
