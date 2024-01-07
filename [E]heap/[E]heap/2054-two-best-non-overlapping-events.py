from heapq import *
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        prev_best = 0
        all_time_best = 0
        for s, e, v in events:
            while heap and heap[0][0] < s:
                prev_end, prev_profit, event_count = heappop(heap)
                if event_count == 1:
                    prev_best = max(prev_best, prev_profit)
            heappush(heap, (e, v, 1))
            heappush(heap, (e, prev_best + v, 2))
            all_time_best = max(all_time_best, prev_best + v)
        return all_time_best
    
# time O(nlogn), due to heap operation is O(logn) and sort is O(nlogn)
# space O(n), due to heap
# using heap and greedily schedule tasks (start/end/val) and sort and greedy