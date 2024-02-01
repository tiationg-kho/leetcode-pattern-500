from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    queue.append((r, c))
                    visited.add((r, c))
        
        while queue:
            r, c = queue.popleft()
            for next_r, next_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if next_r not in range(rows) or next_c not in range(cols) or (next_r, next_c) in visited or board[next_r][next_c] == 'X':
                    continue
                queue.append((next_r, next_c))
                visited.add((next_r, next_c))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'    

# time O(RC)
# space O(RC)
# using graph and bfs with multiple sources