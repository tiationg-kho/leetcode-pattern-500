from heapq import *
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = [(e, s) for e, s in zip(efficiency, speed)]
        eng.sort(key = lambda x: - x[0])

        res = 0
        heap = []
        total_speed = 0
        for e, s in eng:
            total_speed += s
            heappush(heap, s)
            if len(heap) > k:
                total_speed -= heappop(heap)
            res = max(res, e * total_speed)
        return res % (10**9 + 7)
        
# time O(nlogn)
# space O(n + k)
# using heap and focus on stored elements and sort and greedy
'''
two factors in problem, need to handle ony by one
1. we traverse every possible team effi (from high to low), and keep recording the best perf
2. we handle the effi factor by sort, so we can guarantee the effi we use is monotonic dec
3. we handle the spee factor by heap, so we can only store the higher spee and pop the smallest
'''