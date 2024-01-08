from heapq import *
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        min_val, max_val = float('inf'), float('-inf')
        for i, vals in enumerate(nums):
            heappush(heap, (vals[0], i, 0))
            min_val = min(min_val, vals[0])
            max_val = max(max_val, vals[0])

        res = [min_val, max_val]

        while len(heap) == len(nums):
            val, list_idx, val_idx = heappop(heap)
            if val_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][val_idx + 1]
                heappush(heap, (next_val, list_idx, val_idx + 1))

                max_val = max(max_val, next_val)
                min_val = heap[0][0]
                diff = max_val - min_val
                if diff < res[1] - res[0]:
                    res = [min_val, max_val]
               
        return res
    
# time O(nlogk)
# space O(k)
# using heap and k way merge problem and greedy
'''
1. changing the smallest num (start point) can greedily find the small range
'''