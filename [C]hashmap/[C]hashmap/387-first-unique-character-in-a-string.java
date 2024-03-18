class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> charToFreq = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            charToFreq.compute(s.charAt(i), (k, v) -> v == null ? 1 : v + 1);
        }
        for (int i = 0; i < s.length(); i++) {
            if (Objects.equals(charToFreq.get(s.charAt(i)), 1)) {
                return i;
            }
        }
        return - 1;
    }
}

// time O(n), due to traverse twice
// space O(1), due to hashmap (26 letters)
// using hashmap and store sth’s freq