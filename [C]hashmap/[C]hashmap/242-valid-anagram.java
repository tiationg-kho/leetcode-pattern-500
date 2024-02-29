class Solution {
  public boolean isAnagram(String s, String t) {
      if (s.length() != t.length()) {
          return false;
      }
      HashMap<Character, Integer> sCharToFreq = new HashMap<>();
      HashMap<Character, Integer> tCharToFreq = new HashMap<>();
      for (int i = 0; i < s.length(); i++) {
          Character sc = s.charAt(i);
          sCharToFreq.compute(sc, (k, v) -> v == null ? 1 : v + 1);
          Character tc = t.charAt(i);
          tCharToFreq.compute(tc, (k, v) -> v == null ? 1 : v + 1);
      }
      for (Character c: sCharToFreq.keySet()) {
          if (!sCharToFreq.get(c).equals(tCharToFreq.get(c))) {
              return false;
          }
      }
      return true;
  }
}

// time O(n)
// space O(26) == O(1), constant
// using hashmap and store sth’s freq