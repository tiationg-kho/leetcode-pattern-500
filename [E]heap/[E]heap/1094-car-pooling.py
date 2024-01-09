from heapq import *
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        
        seats = capacity
        heap = []
        for p, s, e in trips:
            while heap and heap[0][0] <= s:
                prev_e, prev_p = heappop(heap)
                seats += prev_p
            if seats < p:
                return False
            heappush(heap, (e, p))
            seats -= p
        return True
        
# time O(nlogn), due to sort, and traverse and perform heap operations
# space O(n), due to heap
# using heap and storing and popping out elements and sort
'''
1. sort by start time
2. store (end, passengers) in heap
3. when new passengers come, let old passengers leave (with smallest end time)
'''