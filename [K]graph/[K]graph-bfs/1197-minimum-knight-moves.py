from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        target = (x, y)
        visited = {(0, 0)}
        queue = deque([(0, 0, 0)])
        while queue:
            x, y, step = queue.popleft()
            if (x, y) == target:
                break
            for offset_x, offset_y in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, - 1)]:
                next_x, next_y = x + offset_x, y + offset_y
                if (next_x, next_y) in visited:
                    continue
                if 3 < abs(x - target[0]) + abs(y - target[1]) < abs(next_x - target[0]) + abs(next_y - target[1]):
                    continue
                queue.append((next_x, next_y, step + 1))
                visited.add((next_x, next_y))
        return step

# time O(RC), due to the search's square
# space O(RC), due to set, the queue is O(max(R, C))
# using graph and bfs with single source and pruning