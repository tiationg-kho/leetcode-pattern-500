import bisect
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        for num in nums:
            if not dp or dp[- 1] < num:
                dp.append(num)
            else:
                idx = bisect.bisect_left(dp, num)
                dp[idx] = num
            if len(dp) > 2:
                return True
        return False
    
# time O(n)
# space O(1)
# using dynamic programming and LIS and patience sort and greedy and binary search