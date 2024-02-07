from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for i in range(len(recipes)):
            recipe = recipes[i]
            sources = ingredients[i]
            for s in sources:
                graph[s].append(recipe)
            indegrees[recipe] += len(sources)
            
        queue = deque([])
        for supply in supplies:
            queue.append(supply)
        
        res = []
        while queue:
            node = queue.popleft()
            if node in indegrees:
                res.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return res

# time O(V+E)
# space O(V+E), due to building graph
# using graph and kahn and topological sort