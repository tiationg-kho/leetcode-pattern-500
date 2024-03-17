class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return nums[0];
        }
        if (n == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int prevPrev = nums[0];
        int prev = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) {
            int cur = Math.max(prevPrev + nums[i], prev);
            prevPrev = prev;
            prev = cur;
        }
        return prev;
    }
}

// time O(n), due to traverse
// space O(1)
// using dynamic programming and linear sequence