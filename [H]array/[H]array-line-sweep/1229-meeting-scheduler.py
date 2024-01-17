class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        res = []
        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            if e1 < s2:
                i += 1
            elif e2 < s1:
                j += 1
            else:
                interval = [max(s1, s2), min(e1, e2)]
                if interval[1] - interval[0] >= duration:
                    res.append(interval[0])
                    res.append(interval[0] + duration)
                    break
                elif e1 < e2:
                    i += 1
                else:
                    j += 1
        
        return res
    
# time O(mlogm + nlogn)
# space O(1), not counting built in sort cost
# using array and line sweep and compare two intervals each round and two pointers and greedy and sort

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        intervals = []
        for s, e in slots1:
            if e - s >= duration:
                intervals.append([s, e])
        for s, e in slots2:
            if e - s >= duration:
                intervals.append([s, e])
        intervals.sort()

        res = []
        if intervals:
            prev_s, prev_e = intervals[0]
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if prev_e < cur_s:
                prev_s, prev_e = cur_s, cur_e
            else:
                interval = [max(prev_s, cur_s), min(prev_e, cur_e)]
                if interval[1] - interval[0] >= duration:
                    res.append(interval[0])
                    res.append(interval[0] + duration)
                    break
                if cur_e > prev_e:
                    prev_s, prev_e = cur_s, cur_e
        return res

# time O((m+n)log(m+n))
# space O(m+n)
# using array and line sweep and compare two intervals each round and greedy and sort and prune

from heapq import *
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        events = []
        for s, e in slots1:
            if e - s >= duration:
                events.append((s, 1))
                events.append((e, - 1))
        for s, e in slots2:
            if e - s >= duration:
                events.append((s, 1))
                events.append((e, - 1))

        heapify(events)
        status = 0
        prev_timestamp = 0
        res = []
        while events:
            timestamp, weight = heappop(events)
            if status == 2:
                interval = [prev_timestamp, timestamp]
                if interval[1] - interval[0] >= duration:
                    res.append(interval[0])
                    res.append(interval[0] + duration)
                    break
            prev_timestamp = timestamp
            status += weight
        return res

# time O((m+n)log(m+n))
# space O(m+n)
# using array and line sweep and and greedy and heap and prune