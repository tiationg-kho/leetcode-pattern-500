from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        while queue:
            r, c, step = queue.popleft()
            rooms[r][c] = step
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or rooms[next_r][next_c] == - 1:
                    continue
                queue.append((next_r, next_c, step + 1))
                visited.add((next_r, next_c))
                
# time O(RC)
# space O(RC)
# using graph and bfs with multiple sources