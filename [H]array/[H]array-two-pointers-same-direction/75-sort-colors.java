class Solution {
    public void sortColors(int[] nums) {
        int red = 0;
        int blue = nums.length - 1;
        int i = 0;

        while (i < blue + 1) {
            if (nums[i] == 0) {
                int temp = nums[i];
                nums[i] = nums[red];
                nums[red] = temp;
                i += 1;
                red += 1;
            } else if (nums[i] == 1) {
                i += 1;
            } else {
                int temp = nums[i];
                nums[i] = nums[blue];
                nums[blue] = temp;
                blue -= 1;
            }
        }
    }
}

// time O(n)
// space O(1)
// using array and two pointers same direction and left ptr to record and three way partitioning
/*
1. when swap with left ptr, cur ptr with only get 1 or 0
2. most time is 1. And 0 is when cur ptr swap with left ptr at same idx
3. so cur need plus 1
*/