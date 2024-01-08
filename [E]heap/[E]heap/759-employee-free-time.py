"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        for i, employee in enumerate(schedule):
            heappush(heap, (schedule[i][0].start, schedule[i][0].end, i, 0))

        res = []
        prev_end = 0
        while heap:
            s, e, employee_id, interval_id = heappop(heap)
            if prev_end and prev_end < s:
                res.append(Interval(prev_end, s))
            prev_end = max(prev_end, e)
            if interval_id + 1 < len(schedule[employee_id]):
                interval = schedule[employee_id][interval_id + 1]
                heappush(heap, (interval.start, interval.end, employee_id, interval_id + 1))
        return res
    
# time O(nlogk)
# space O(k), due to heap
# using heap and k way merge problem and interval