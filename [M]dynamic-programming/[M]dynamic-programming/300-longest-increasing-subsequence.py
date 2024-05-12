class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for end in range(len(nums)):
            for start in range(end):
                if nums[start] < nums[end]:
                    dp[end] = max(dp[end], dp[start] + 1)
        return max(dp)

# time O(n**2), due to each num has run a loop to check the nums before it
# space O(n), due to dp list
# using dynamic programming and linear sequence
'''
1. dp[i] means the length of LIS which ends in i
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

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

        dp = []
        for i, num in enumerate(nums):
            if not dp or dp[- 1] < num:
                dp.append(num)
            else:
                idx = find_first_larger_or_equal(dp, num)
                dp[idx] = num
        return len(dp)

# time O(nlogn), due to binary search costs logn and traverse every num
# space O(n), due to dp list
# using dynamic programming and LIS and patience sort and greedy and binary search
'''
1. dp[i] means the smallest last num when subseq's length is i+1
2. this num should greedily find out the smallest one
3. when new num is greater than last one means subsequence can grow
4. else have to find this num can help which length's subsequence improve
'''