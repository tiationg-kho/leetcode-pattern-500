class Solution {
    public int maxSubArray(int[] nums) {
        int res = Integer.MIN_VALUE;
        int total = 0;
        for (int num: nums) {
            total += num;
            res = Math.max(res, total);
            if (total < 0) {
                total = 0;
            }
        }
        return res;
    }
}

// time O(n)
// space O(1)
// using greedy