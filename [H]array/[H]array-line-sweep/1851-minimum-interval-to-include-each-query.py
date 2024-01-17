from heapq import *
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()
        res = [- 1 for _ in range(len(queries))]

        heap = []
        idx = 0
        for q, i in queries:
            while idx < len(intervals):
                s, e = intervals[idx]
                if q < s:
                    break
                elif e < q:
                    idx += 1
                else:
                    heappush(heap, (e - s + 1, s, e))
                    idx += 1
            
            while heap:
                length, s, e = heap[0]
                if e < q:
                    heappop(heap)
                else:
                    res[i] = length
                    break
        return res
    
# time O(nlogn + qlogq)
# space O(n + q)
# using array and line sweep and heap to store previous intervals’ states and greedy and sort