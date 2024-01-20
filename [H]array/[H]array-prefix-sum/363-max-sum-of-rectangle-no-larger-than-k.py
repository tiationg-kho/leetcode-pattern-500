from sortedcontainers import SortedDict
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for r in range(rows):
            total = 0
            for c in range(cols):
                total += matrix[r][c]
                prefix[r + 1][c + 1] = total
        
        def get_sum(part_rows):
            prefix_dict = SortedDict()
            prefix_dict[0] = - 1
            total = 0
            res = float('-inf')
            for r, part_row in enumerate(part_rows):
                total += part_row
                idx = prefix_dict.bisect_left(total - k)
                if idx < len(prefix_dict):
                    res = max(res, total - prefix_dict.peekitem(idx)[0])
                if total not in prefix_dict:
                    prefix_dict[total] = r
            return res

        res = float('-inf')
        for lc in range(cols):
            for rc in range(lc, cols):
                part_rows = [row[rc + 1] - row[lc] for i, row in enumerate(prefix) if i > 0]
                res = max(res, get_sum(part_rows))
        return res
    
# time O(C**2 * RlogR)
# space O(RC)
# using array and prefix sum and hashmap to validate the gap subarray and binary search