from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows, cols = len(board), len(board[0])
        
        def get_rc(num):
            num -= 1
            r, c = divmod(num, cols)
            if r % 2:
                c = cols - 1 - c
            r = rows - 1 - r
            return (r, c)

        visited = set()
        queue = deque([(1, 0)])
        visited.add(1)
        while queue:
            num, step = queue.popleft()
            r, c = get_rc(num)
            if board[r][c] != - 1:
                num = board[r][c]
            if num == rows * cols:
                return step
            for offset in range(1, 7):
                next_num = num + offset
                if next_num in visited:
                    continue
                queue.append((next_num, step + 1))
                visited.add(next_num)

        return - 1
    
# time O(RC)
# space O(RC)
# using graph and bfs with single source