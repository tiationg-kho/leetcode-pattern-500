class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> scToTc = new HashMap<>();
        HashMap<Character, Character> tcToSc = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character sc = s.charAt(i);
            Character tc = t.charAt(i);
            if (!scToTc.containsKey(sc)) {
                scToTc.put(sc, tc);
            }
            if (!tcToSc.containsKey(tc)) {
                tcToSc.put(tc, sc);
            }
            if (!Objects.equals(sc, tcToSc.get(tc))) {
                return false;
            }
            if (!Objects.equals(tc, scToTc.get(sc))) {
                return false;
            }
        }
        return true;
    }
}

// time O(n), due to traverse
// space O(n), can be O(1) since char's number is limited
// using hashmap and build bijection mapping relation