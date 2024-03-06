class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        int max = Integer.MAX_VALUE;
        Arrays.fill(dp, max);
        dp[0] = 0;

        for (int i = 0; i < coins.length; i++) {
            for (int j = 1; j < amount + 1; j++) {
                if (coins[i] <= j) {
                    int cand = dp[j - coins[i]] == max ? max : dp[j - coins[i]] + 1;
                    dp[j] = Math.min(dp[j], cand);
                }
            }
        }
        return dp[amount] == max ? - 1 : dp[amount];
    }
}

// time O(m * n), m is the amount and n is the number of coins
// space O(m), due to the dp list's size
// using dynamic programming and knapsack (complete knapsack) 