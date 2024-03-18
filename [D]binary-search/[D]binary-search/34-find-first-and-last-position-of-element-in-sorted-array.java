class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[2];

        int left = 0;
        int right = nums.length - 1;
        int boundary = - 1;
        while (left <= right) {
            int m = left + (right - left) / 2;
            if (nums[m] == target) {
                boundary = m;
                right = m - 1;
            } else if (nums[m] > target) {
                right = m - 1;
            } else {
                left = m + 1;
            }
        }
        res[0] = boundary;

        left = 0;
        right = nums.length - 1;
        boundary = - 1;
        while (left <= right) {
            int m = left + (right - left) / 2;
            if (nums[m] == target) {
                boundary = m;
                left = m + 1;
            } else if (nums[m] > target) {
                right = m - 1;
            } else {
                left = m + 1;
            }
        }
        res[1] = boundary;
        return res;
    }
}

// time O(logn)
// space O(1)
// using binary search and search in a sorted array for specific val