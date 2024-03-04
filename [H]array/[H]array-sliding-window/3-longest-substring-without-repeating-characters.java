class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> charToFreq = new HashMap<>();
        int res = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            Character c = s.charAt(right);
            charToFreq.compute(c, (k, v) -> v == null ? 1 : v + 1);
            while (charToFreq.get(c) > 1) {
                Character removeC = s.charAt(left);
                charToFreq.put(removeC, charToFreq.get(removeC) - 1);
                if (Objects.equals(charToFreq.get(removeC), 0)) {
                    charToFreq.remove(removeC);
                }
                left += 1;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}

// time O(n)
// space O(1), due to the hashmap could contain all unique chars
// using array and standard sliding window and hashmap