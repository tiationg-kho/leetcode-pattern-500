class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = []
        prev_s, prev_e = intervals[0]
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if prev_e < cur_s:
                res.append([prev_s, prev_e])
                prev_s, prev_e = cur_s, cur_e
            else:
                prev_e = max(prev_e, cur_e)

        res.append([prev_s, prev_e])

        return res
        
# time O(nlogn)
# space O(n), due to output and sort
# using array and line sweep and compare two intervals each round and sort

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        events = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e, - 1))
        events.sort(key = lambda x: (x[0], - x[1]))

        res = []
        status = 0
        prev_timestamp = 0

        for timestamp, weight in events:
            if status == 0 and weight == 1:
                prev_timestamp = timestamp
            if status == 1 and weight == - 1:
                res.append([prev_timestamp, timestamp])
            status += weight

        return res
                
# time O(nlogn)
# space O(n), due to output and sort
# using array and line sweep and sort
'''
1. if certain timestamp have both start and end event, let start event become first
'''
