from heapq import *
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort()

        heap = []
        prev_best = 0
        all_time_best = 0
        for s, e, p in jobs:
            while heap and heap[0][0] <= s:
                _, prev_p = heappop(heap)
                prev_best = max(prev_best, prev_p)
            heappush(heap, (e, prev_best + p))
            all_time_best = max(all_time_best, prev_best + p)
        return all_time_best
        
# time O(nlogn), due to heap operation is O(logn) and sort is O(nlogn)
# space O(n), due to heap
# using heap and greedily schedule tasks (start/end/val) and sort and greedy
'''
- sort every task by their start time
- use heap to quickly find the most recent finished task according to cur task
- use pop out elements to keep recording the previous best result
  - the previous best result is according to cur task (also applicable for future tasks to use)
- push the cur end time and cur result in heap for future tasks
  - when pushing also treat this profit as a candidate of best result
  - we need to keep recording the all time best result
'''