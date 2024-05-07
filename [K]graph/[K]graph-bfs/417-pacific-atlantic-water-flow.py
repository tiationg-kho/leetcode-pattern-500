from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        g = heights
        rows, cols = len(g), len(g[0])

        def bfs(queue, visited, temp):
            while queue:
                r, c = queue.popleft()
                temp[r][c] += 1
                for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or g[r][c] > g[next_r][next_c]:
                        continue
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))
        
        temp = [[0 for _ in range(cols)] for _ in range(rows)]
        p_queue = deque([])
        p_visited = set()
        a_queue = deque([])
        a_visited = set()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    p_queue.append((r, c))
                    p_visited.add((r, c))
                if r == rows - 1 or c == cols - 1:
                    a_queue.append((r, c))
                    a_visited.add((r, c))
        bfs(p_queue, p_visited, temp)
        bfs(a_queue, a_visited, temp)
        res = []
        for r in range(rows):
            for c in range(cols):
                if temp[r][c] == 2:
                    res.append([r, c])
        return res
    
# time O(RC)
# space O(RC)
# using graph and bfs with multiple sources