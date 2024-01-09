from heapq import *
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(-((p+1)/(t+1) - p/t), p, t) for p, t in classes]
        heapify(heap)

        while extraStudents:
            _, p, t = heappop(heap)
            heappush(heap, (-((p+2)/(t+2) - (p+1)/(t+1)), p + 1, t + 1))
            extraStudents -= 1
        
        ratio = 0
        for _, p, t in heap:
            ratio += p/t
        return ratio / len(classes)

# time O(n + mlogn)
# space O(n)
# using heap and storing and popping out elements