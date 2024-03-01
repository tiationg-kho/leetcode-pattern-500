class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int prevPrev = 1;
        int prev = 2;
        for (int i = 3; i < n + 1; i++) {
            int cur = prevPrev + prev;
            int temp = prev;
            prev = cur;
            prevPrev = temp;
        }
        return prev;
    }
}

// time O(n)
// space O(1)
// using dynamic programming and linear sequence