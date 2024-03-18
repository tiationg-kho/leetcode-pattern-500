class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        HashMap<Integer, Integer> valToFreq = new HashMap<>();
        valToFreq.put(0, 1);
        int total = 0;
        for (int num: nums) {
            total += num;
            if (valToFreq.containsKey(total - k)) {
                res += valToFreq.get(total - k);
            }
            valToFreq.compute(total, (key, v) -> v == null ? 1 : v + 1);
        }
        return res;
    }
}

// time O(n)
// space O(n)
// using array and prefix sum and hashmap to validate the gap subarray
/*
1. if meet the prefix - k in hashmap means the gap is valid
*/