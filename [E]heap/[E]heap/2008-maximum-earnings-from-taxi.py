from heapq import *
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()

        heap = []
        prev_best = 0
        all_time_best = 0
        for s, e, t in rides:
            while heap and heap[0][0] <= s:
                prev_end, prev_profit = heappop(heap)
                prev_best = max(prev_best, prev_profit)
            heappush(heap, (e, prev_best + e - s + t))
            all_time_best = max(all_time_best, prev_best + e - s + t)
        return all_time_best

# time O(nlogn), due to heap operation is O(logn) and sort is O(nlogn)
# space O(n), due to heap
# using heap and greedily schedule tasks (start/end/val) and sort and greedy