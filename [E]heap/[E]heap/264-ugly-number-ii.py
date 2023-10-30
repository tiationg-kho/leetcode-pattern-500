from heapq import *
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        prime = [2, 3, 5]
        res = [1]
        heap = [(res[0] * prime[i], 0, i) for i in range(len(prime))]
        while len(res) < n:
            num, root_idx, prime_idx = heappop(heap)
            if num > res[- 1]:
                res.append(num)
            heappush(heap, (res[root_idx + 1] * prime[prime_idx], root_idx + 1, prime_idx))
        return res[- 1]
    
# time O((nk)*logk), k is 3
# space O(n + k)
# using heap and k way merge problem
'''
1. imagine 3 sorted list to do merging
'''