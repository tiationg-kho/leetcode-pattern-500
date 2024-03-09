class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> charToFreq = new HashMap<>();
        int max = 0;
        int res = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            Character c = s.charAt(right);
            charToFreq.compute(c, (key, v) -> v == null ? 1 : v + 1);
            if (charToFreq.get(c) > max) {
                max = charToFreq.get(c);
            }
            while (max + k < right - left + 1) {
                Character remove_c = s.charAt(left);
                charToFreq.put(remove_c, charToFreq.get(remove_c) - 1);
                if (charToFreq.get(remove_c) == 0) {
                    charToFreq.remove(remove_c);
                }
                left += 1;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}

// time O(n)
// space O(1)
// using array and standard sliding window and hashmap and greedy