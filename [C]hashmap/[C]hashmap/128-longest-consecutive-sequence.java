class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num: nums) {
            set.add(num);
        }
        int res = 0;
        for (int num: nums) {
            if (set.contains(num - 1)) {
                continue;
            }
            int left = num;
            int right = num;
            if (!set.contains(left + res)) {
                continue;
            }
            while (set.contains(right + 1)) {
                right += 1;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}

// time O(n)
// sapce O(n)
// using hashmap and store val and hashset and pruning
/*
1. find every sequence's start point
*/