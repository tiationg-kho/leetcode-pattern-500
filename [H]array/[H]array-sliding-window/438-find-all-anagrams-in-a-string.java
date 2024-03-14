class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        HashMap<Character, Integer> pcharToFreq = new HashMap<>();
        for (int i = 0; i < p.length(); i++) {
            pcharToFreq.compute(p.charAt(i), (k, v) -> v == null ? 1 : v + 1);
        }
        HashMap<Character, Integer> subcharToFreq = new HashMap<>();
        int total = pcharToFreq.size();
        int match = 0;
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            subcharToFreq.compute(s.charAt(right), (k, v) -> v == null ? 1 : v + 1);
            if (Objects.equals(subcharToFreq.get(s.charAt(right)), pcharToFreq.get(s.charAt(right)))) {
                match += 1;
            }
            while (right - left + 1 > p.length()) {
                Character c = s.charAt(left);
                if (Objects.equals(subcharToFreq.get(c), pcharToFreq.get(c))) {
                    match -= 1;
                }
                subcharToFreq.put(c, subcharToFreq.get(c) - 1);
                if (Objects.equals(subcharToFreq.get(c), 0)) {
                    subcharToFreq.remove(c);
                }
                left += 1;
            }
            if (match == total) {
                res.add(left);
            }
        }
        return res;
    }
}

// time O(m+n), due to traverse
// space O(1), not counting output
// using array and standard sliding window and hashmap