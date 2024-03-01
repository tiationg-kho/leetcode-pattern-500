class Solution {
    public int majorityElement(int[] nums) {
        Integer cand = null;
        int vote = 0;
        for (int i = 0; i < nums.length; i++) {
            if (cand != null && cand == nums[i]) {
                vote += 1;
            } else if (cand == null) {
                cand = nums[i];
                vote = 1;
            } else {
                vote -= 1;
                if (vote == 0) {
                    cand = null;
                }
            }
        }
        return cand;
    }
}

// time O(n)
// space O(1)
// using array and boyer moore vote algorithm