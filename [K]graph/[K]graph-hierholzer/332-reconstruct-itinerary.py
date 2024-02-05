from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for p, q in sorted(tickets, reverse=True):
            graph[p].append(q)

        stack = []
        def dfs(node):
            while graph[node]:
                neighbor = graph[node].pop()
                dfs(neighbor)
            stack.append(node)
        
        dfs("JFK")
        
        path = []
        while stack:
            path.append(stack.pop())
        return path

# time O(ElogE), due to sort
# space O(V + E)
# using graph and hierholzer and eulerian path