class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            if (i % 2 == 1) {
                res[i] = res[i / 2] + 1;
            } else {
                res[i] = res[i / 2];
            }
        }
        return res;
    }
}

// time O(n)
// space O(n)
// using math