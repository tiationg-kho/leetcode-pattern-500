from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        val_indices = defaultdict(list)
        for i, val in enumerate(arr):
            val_indices[val].append(i)
        visited = {0}
        queue = deque([(0, 0)])
        while queue:
            i, step = queue.popleft()
            if i == len(arr) - 1:
                return step
            for next_idx in [i - 1, i + 1] + val_indices[arr[i]]:
                if next_idx not in range(len(arr)) or next_idx in visited:
                    continue
                queue.append((next_idx, step + 1))
                visited.add(next_idx)
            val_indices.pop(arr[i])
            
# time O(n)
# space O(n)
# using graph and bfs with single source and pruning