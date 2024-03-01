class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                continue;
            }
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left += 1;
        }
    }
}

// time O(n)
// space O(1)
// using array and two pointers same direction and left ptr to record