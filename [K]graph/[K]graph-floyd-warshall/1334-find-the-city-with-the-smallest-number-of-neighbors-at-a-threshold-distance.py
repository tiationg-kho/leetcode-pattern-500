class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        for p, q, w in edges:
            dist[p][q] = w
            dist[q][p] = w
        for i in range(n):
            dist[i][i] = 0

        for mid in range(n):
            for start in range(n):
                for end in range(n):
                    if dist[start][mid] + dist[mid][end] < dist[start][end]:
                        dist[start][end] = dist[start][mid] + dist[mid][end]
        
        res = 0
        res_count = n
        for i in range(n):
            count = 0
            for j in range(n):
                if i == j:
                    continue
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if count <= res_count:
                res_count = count
                res = i
        return res
    
# time O(V**3)
# space O(V**2)
# using graph and floyd warshall and shortest path