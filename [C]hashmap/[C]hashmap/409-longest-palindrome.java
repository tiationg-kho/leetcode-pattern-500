class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> charToFreq = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            charToFreq.compute(c, (k, v) -> v == null ? 1 : v + 1);
        }

        int res = 0;
        for (Map.Entry<Character, Integer> kv: charToFreq.entrySet()) {
            Character k = kv.getKey();
            Integer v = kv.getValue();
            if (res % 2 == 0) {
                res += v;
            } else {
                if (v % 2 == 1) {
                    v -= 1;
                }
                res += v;
            }
        }
        return res;
    }
}

// time O(n)
// space O(1)
// using hashmap and store sth’s freq