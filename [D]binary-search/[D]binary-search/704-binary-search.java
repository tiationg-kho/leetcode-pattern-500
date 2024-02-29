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
            } else if (nums[m] > target) {
                right = m - 1;
            } else {
                left = m + 1;
            }
        }
        return boundary;
    }
}

// time O(logn), n is the length of nums
// space O(1)
// using binary search and search in a sorted array for specific val