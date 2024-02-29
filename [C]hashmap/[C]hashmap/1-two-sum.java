class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> valToIdx = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (valToIdx.containsKey(target - nums[i])) {
                return new int[]{valToIdx.get(target - nums[i]), i};
            }
            valToIdx.put(nums[i], i);
        }
        return null;
    }
}

// time O(n), due to traverse
// space O(n), due to hashmap
// using hashmap and store val