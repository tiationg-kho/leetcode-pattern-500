class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        def find_first_larger(vals, num):
            left, right, boundary = 0, len(vals) - 1, - 1
            while left <= right:
                m = (left + right) // 2
                if num < vals[m]:
                    boundary = m
                    right = m - 1
                else:
                    left = m + 1
            return boundary

        o = obstacles
        res = [1 for _ in range(len(o))]
        dp = []
        for i, num in enumerate(o):
            if not dp or dp[- 1] <= num:
                dp.append(num)
                res[i] = len(dp)
            else:
                idx = find_first_larger(dp, num)
                dp[idx] = num
                res[i] = idx + 1
        return res

# time O(nlogn), due to binary search costs logn and traverse every num
# space O(n), due to dp list
# using dynamic programming and LIS and patience sort and greedy and binary search
'''
1. dp[i] means the smallest last num when subseq's length is i+1
2. this num should greedily find out the smallest one
3. when new num is greater or equal than last one means subsequence can grow
4. else have to find this num can help which length's subsequence improve
'''