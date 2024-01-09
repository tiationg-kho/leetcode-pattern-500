from heapq import *
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        engineers = [(s, e) for s, e in zip(speed, efficiency)]
        engineers.sort(key = lambda x: - x[1])

        res = 0
        total = 0
        heap = []
        for s, e in engineers:
            total += s
            heappush(heap, s)
            if len(heap) > k:
                total -= heappop(heap)
            res = max(res, total * e)

        return res % (10**9+7)
        
# time O(nlogn)
# space O(n + k)
# using heap and storing and popping out elements and sort and greedy
'''
two factors in problem, need to handle ony by one
1. we traverse every possible team effi (from high to low), and keep recording the best perf
2. we handle the effi factor by sort, so we can guarantee the effi we use is monotonic dec
3. we handle the spee factor by heap, so we can only store the higher spee and pop the smallest
'''