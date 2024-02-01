from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_route = defaultdict(list)
        for i, r in enumerate(routes):
            for stop in r:
                stop_route[stop].append(i)
        
        visited = set()
        queue = deque([(source, 0)])
        while queue:
            stop, step = queue.popleft()
            if stop == target:
                return step
            for r in stop_route[stop]:
                if r in visited:
                    continue
                visited.add(r)
                for stop in routes[r]:
                    queue.append((stop, step + 1))
                    
        return - 1
        
# time (n*m)
# space O(n*m), due to building graph, n is the number of routes, m is the number of stops
# using graph and bfs with single source
'''
1. when building graph, using bus route instead of bus stop
'''