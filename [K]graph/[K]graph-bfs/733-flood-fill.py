from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        old_color = image[sr][sc]
        visited = set()
        queue = deque([(sr, sc)])
        visited.add((sr, sc))
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or image[next_r][next_c] != old_color:
                    continue
                queue.append((next_r, next_c)) 
                visited.add((next_r, next_c))
        return image

# time O(RC)
# space O(RC)
# using graph and bfs with single source