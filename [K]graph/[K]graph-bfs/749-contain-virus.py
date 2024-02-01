from collections import deque
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        g = isInfected
        rows, cols = len(g), len(g[0])
        
        def bfs(row, col):
            old_area = set()
            new_area = set()
            walls = 0
            queue = deque([(row, col)])
            old_area.add((row, col))
            while queue:
                r, c = queue.popleft()
                for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in old_area:
                        continue
                    if g[next_r][next_c] == 0:
                        walls += 1
                        new_area.add((next_r, next_c))
                    elif g[next_r][next_c] == 1:
                        queue.append((next_r, next_c))
                        old_area.add((next_r, next_c))
            return walls, old_area, new_area
        
        res = 0
        while True:
            idx_info = {}
            visited = set()
            idx = 0
            for r in range(rows):
                for c in range(cols):
                    if g[r][c] != 1 or (r, c) in visited:
                        continue
                    walls, old_area, new_area = bfs(r, c)
                    idx_info[idx] = (walls, old_area, new_area)
                    for row, col in old_area:
                        visited.add((row, col))
                    idx += 1
            if not idx_info:
                break
            target = max(idx_info.keys(), key = lambda x: len(idx_info[x][2]))
            walls, old_area, new_area = idx_info[target]
            res += walls
            for row, col in old_area:
                g[row][col] = 2
            idx_info.pop(target)
            for walls, old_area, new_area in idx_info.values():
                for row, col in new_area:
                    g[row][col] = 1
        return res
    
# time O(RC * (R + C)), each day cost RC and (R+C) days at most
# space O(RC)
# using graph and bfs with single source and hashmap