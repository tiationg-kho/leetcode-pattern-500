class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int boundary = - 1;
        while (left <= right) {
            int m = left + (right - left) / 2;
            if (nums[m] >= target) {
                boundary = m;
                right = m - 1;
            } else {
                left = m + 1;
            }
        }
        return boundary != - 1 ? boundary : nums.length;
    }
}

// time O(logn)
// space O(1)
// using binary search and search in a sorted array for most close val