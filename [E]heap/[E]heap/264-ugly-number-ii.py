from heapq import *
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        primes = [2, 3, 5]
        heap = [(res[0] * primes[i], 0, i) for i in range(len(primes))]
        while len(res) < n:
            val, res_idx, primes_idx = heappop(heap)
            if val > res[- 1]:
                res.append(val)
            heappush(heap, (res[res_idx + 1] * primes[primes_idx], res_idx + 1, primes_idx))
        return res[- 1]
    
# time O(nklog(k)), k is 3
# space O(n + k)
# using heap and k way merge problem
'''
1. imagine 3 virtual sorted lists to do merging
2. we dynamically generate these 3 sorted lists from our current res list
'''