class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def find_first_larger_or_equal(vals, num):
            left, right, boundary = 0, len(vals) - 1, - 1
            while left <= right:
                m = (left + right) // 2
                if num <= vals[m]:
                    boundary = m
                    right = m - 1
                else:
                    left = m + 1
            return boundary

        envelopes.sort(key = lambda x: (x[0], - x[1]))
        dp = []
        for w, h in envelopes:
            if not dp or dp[- 1] < h:
                dp.append(h)
            else:
                idx = find_first_larger_or_equal(dp, h)
                dp[idx] = h

        return len(dp)
    
# time O(nlogn)
# space O(n)
# using dynamic programming and LIS and patience sort and greedy and binary search and sort
'''
1. notice the condition of sorting
'''