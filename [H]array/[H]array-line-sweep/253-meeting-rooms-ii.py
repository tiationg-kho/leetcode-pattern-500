from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        heap = []
        for s, e in intervals:
            if heap and heap[0] <= s:
                heappop(heap)
            heappush(heap, e)
        return len(heap)

# time O(nlogn)
# space O(n)
# using array and line sweep and heap to store previous intervals’ states

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        heap = []
        res = 0
        for s, e in intervals:
            while heap and heap[0] <= s:
                heappop(heap)
            heappush(heap, e)
            res = max(res, len(heap))
        return res

# time O(nlogn)
# space O(n)
# using array and line sweep and heap to store previous intervals’ states

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        events = []

        for s, e in intervals:
            events.append((s, 1))
            events.append((e, - 1))
        events.sort()

        status = 0
        res = 0
        for timestamp, weight in events:
            status += weight
            res = max(res, status)
        return res

# time O(nlogn)
# space O(n)
# using array and line sweep and sort