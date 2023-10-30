from heapq import *
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res = 0
        heap = []
        for i in range(len(apples)):
            count = apples[i]
            expire = i + days[i]
            if count:
                heappush(heap, [expire, count])
            while heap and (heap[0][0] <= i or heap[0][1] == 0):
                heappop(heap)
            if heap and heap[0][1] > 0:
                res += 1
                heap[0][1] -= 1

        cur_day = len(apples)
        while heap:
            expire, count = heappop(heap)
            if expire <= cur_day:
                continue
            eat = min(count, expire - cur_day)
            res += eat
            cur_day += eat
        return res
    
# time O(nlogn)
# space O(n)
# using heap and focus on popping out