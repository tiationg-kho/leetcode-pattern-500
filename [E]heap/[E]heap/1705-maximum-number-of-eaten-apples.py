from heapq import *
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        res = 0
        for i in range(len(apples)):
            while heap and heap[0][0] <= i:
                heappop(heap)
            if apples[i] != 0:
                heappush(heap, [i + days[i], apples[i]])
            if heap and heap[0][1] > 0:
                res += 1
                heap[0][1] -= 1
                if heap[0][1] == 0:
                    heappop(heap)

        cur = len(apples)
        while heap:
            while heap and heap[0][0] <= cur:
                heappop(heap)
            if heap:
                end, count = heappop(heap)
                res += min(end - cur, count)
                cur += min(end - cur, count)

        return res
    
# time O(nlogn)
# space O(n)
# using heap and storing and popping out elements