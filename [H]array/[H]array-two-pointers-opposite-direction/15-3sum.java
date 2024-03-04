class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i - 1 >= 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            int j = i + 1;
            int k = nums.length - 1;
            int target = 0 - nums[i];
            if (nums[j] + nums[j + 1] > target) {
                break;
            }
            if (nums[k - 1] + nums[k] < target) {
                continue;
            }
            while (j < k) {
                int total = nums[j] + nums[k];
                if (total == target) {
                    res.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k])));
                    j += 1;
                    k -= 1;
                } else if (total > target) {
                    k -= 1;
                } else {
                    j += 1;
                }
                while (j < k && j - 1 > i && nums[j - 1] == nums[j]) {
                    j += 1;
                }
                while (j < k && k + 1 < nums.length && nums[k] == nums[k + 1]) {
                    k -= 1;
                }
            }
        }
        return res;
    }
}

// time O(n**2)
// space O(1), or due to built in sort's cost
// using array and two pointers opposite direction and shrink type and sort
/*
1. be aware of handling duplicate
*/