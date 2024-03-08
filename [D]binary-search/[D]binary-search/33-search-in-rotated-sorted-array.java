class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int boundary = - 1;
        while (left <= right) {
            int m = left + (right - left) / 2;
            if (nums[m] == target) {
                boundary = m;
                break;
            }
            if (nums[m] > nums[right]) {
                if (nums[left] <= target && target < nums[m]) {
                    right = m - 1;
                } else {
                    left = m + 1;
                }
            } else {
                if (nums[m] < target && target <= nums[right]) {
                    left = m + 1;
                } else {
                    right = m - 1;
                }
            }
        }
        return boundary;
    }
}

// time O(logn)
// space O(1)
// using binary search and rotated sorted array
/*
1. compare to right ptr
2. if m ptr val larger than right ptr val, means the left side of m ptr has order
3. if m ptr val less than right ptr val, means the right side of m ptr has order
*/