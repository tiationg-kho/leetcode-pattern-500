from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacifics = [[False for _ in range(cols)] for _ in range(rows)]
        atlantics = [[False for _ in range(cols)] for _ in range(rows)]
        pacific_nodes = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic_nodes = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        def bfs(nodes, ocean):
            visited = set()
            queue = deque([])
            for node in nodes:
                queue.append(node)
                visited.add(node)
            while queue:
                r, c = queue.popleft()
                ocean[r][c] = True
                for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or heights[r][c] > heights[next_r][next_c]:
                        continue
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))
        
        bfs(pacific_nodes, pacifics)
        bfs(atlantic_nodes, atlantics)
        res = []
        for r in range(rows):
            for c in range(cols):
                if pacifics[r][c] and atlantics[r][c]:
                    res.append([r, c])
        return res
    
# time O(RC)
# space O(RC)
# using graph and bfs with multiple sources