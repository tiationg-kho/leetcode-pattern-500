class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# time O(n**2), due to each num has run a loop to check the nums before it
# space O(n), due to dp list
# using dynamic programming and linear sequence
'''
1. dp[i] means the length of LIS which ends in i
'''

import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or dp[- 1] < num:
                dp.append(num)
            else:
                idx = bisect.bisect_left(dp, num)
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