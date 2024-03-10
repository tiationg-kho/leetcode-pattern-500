class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> set = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int start = 0; start < s.length(); start++) {
            for (int end = start; end < s.length(); end++) {
                if (set.contains(s.substring(start, end + 1))) {
                    dp[end + 1] |= dp[start];
                }
            }
        }
        return dp[s.length()];
    }
}

// time O(n**3), due to two nested lopp and slice string
// space O(n + m), due to dp list and hashset
// using dynamic programming and linear sequence