from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap_validate = []
        for p, c in zip(profits, capital):
            minheap_validate.append((c, p))
        heapify(minheap_validate)

        maxheap_profitable = []
        while k:
            while minheap_validate and minheap_validate[0][0] <= w:
                c, p = heappop(minheap_validate)
                heappush(maxheap_profitable, - p)
            if maxheap_profitable:
                neg_p = heappop(maxheap_profitable)
                w += - neg_p
                k -= 1
            else:
                break
        return w

# time O(nlogn)
# space O(n)
# using heap and two heap problem