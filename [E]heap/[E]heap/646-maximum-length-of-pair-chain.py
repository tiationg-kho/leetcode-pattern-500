from heapq import *
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        heap = []
        prev_best = 0
        all_time_best = 0
        for s, e in pairs:
            while heap and heap[0][0] < s:
                _, prev_len = heappop(heap)
                prev_best = max(prev_best, prev_len)
            heappush(heap, (e, prev_best + 1))
            all_time_best = max(all_time_best, prev_best + 1)
        return all_time_best
    
# time O(nlogn), due to heap operation is O(logn) and sort is O(nlogn)
# space O(n), due to heap
# using heap and greedily schedule tasks (start/end/val) and sort and greedy