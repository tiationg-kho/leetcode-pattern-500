class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int num: nums) {
            res ^= num;
        }
        return res;
    }
}

// time O(n)
// space O(1)
// using bit manipulation and xor