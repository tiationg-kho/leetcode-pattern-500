from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            heappush(heap, (- distance, x, y))
            if len(heap) > k:
                heappop(heap)
                
        return [[x, y] for _, x, y in heap]

# time O(nlogk)
# space O(k)
# using heap and top k problem (based on heap) and max heap