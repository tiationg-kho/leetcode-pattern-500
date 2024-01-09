from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heap = []
        visited = set()
        heappush(heap, (matrix[0][0], 0, 0))
        visited.add((0, 0))
        while k:
            val, r, c = heappop(heap)
            k -= 1
            if r + 1 < rows and (r + 1, c) not in visited:
                heappush(heap, (matrix[r+1][c], r + 1, c))
                visited.add((r + 1, c))
            if c + 1 < cols and (r, c + 1) not in visited:
                heappush(heap, (matrix[r][c+1], r, c + 1))
                visited.add((r, c + 1))
        return val

# time O(klogk)
# space O(k)
# using heap and bfs