class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> rCharToFreq = new HashMap<>();
        HashMap<Character, Integer> mCharToFreq = new HashMap<>();
        for (int i = 0; i < ransomNote.length(); i++) {
            Character c = ransomNote.charAt(i);
            rCharToFreq.compute(c, (k, v) -> v == null ? 1 : v + 1);
        }
        for (int i = 0; i < magazine.length(); i++) {
            Character c = magazine.charAt(i);
            mCharToFreq.compute(c, (k, v) -> v == null ? 1 : v + 1);
        }
        for (Character c: rCharToFreq.keySet()) {
            if (mCharToFreq.containsKey(c) && rCharToFreq.get(c) <= mCharToFreq.get(c)) {
                continue;
            }
            return false;
        }
        return true;
    }
}

// time O(n+m)
// space O(26) == O(1), constant
// using hashmap and store sth’s freq