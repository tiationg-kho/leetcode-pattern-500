class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        Arrays.fill(res, 1);
        int total = 1;
        for (int i = 0; i < nums.length; i++) {
            res[i] = total;
            total *= nums[i];
        }
        total = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= total;
            total *= nums[i];
        }
        return res;
    }
}

// time O(n)
// space O(1), not counting output list
// using array and prefix sum and standard prefix sum