class Solution {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int num: nums) {
            total += num;
        }
        if (total % 2 == 1) {
            return false;
        }
        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num: nums) {
            for (int t = target; t >= 0; t--) {
                if (t >= num) {
                    dp[t] |= dp[t - num];
                }
            }
        }
        return dp[target];
    }
}

// time O(nm), n is the number of nums
// space O(m), m is the sum of all elements in nums
// using dynamic programming and knapsack (0-1 knapsack) 