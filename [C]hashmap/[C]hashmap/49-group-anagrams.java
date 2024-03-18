class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> patternToStrings = new HashMap<>();
        for (String s: strs) {
            int[] charToFreq = new int[26];
            for (int i = 0; i < s.length(); i++) {
                charToFreq[s.charAt(i) - 'a'] += 1;
            }
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < 26; i++) {
                sb.append("#");
                sb.append(charToFreq[i]);
            }
            patternToStrings.computeIfAbsent(sb.toString(), k -> new ArrayList<>()).add(s);
        }
        List<List<String>> res = new ArrayList<>();
        for (ArrayList<String> val: patternToStrings.values()) {
            res.add(val);
        }
        return res;
    }
}

// time O(nL)
// space O(nL)
// using hashmap and store sth’s freq