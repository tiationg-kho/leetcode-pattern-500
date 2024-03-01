class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        for (String s: strs) {
            if (s.length() < prefix.length()) {
                prefix = s;
            }
        }
        for (int i = 0; i < prefix.length(); i++) {
            for (String s: strs) {
                if (prefix.charAt(i) != s.charAt(i)) {
                    return prefix.substring(0, i);
                }
            }
        }
        return prefix;
    }
}

// time O(nL)
// space O(1)
// using string and string composition
/*
1. notice the order of for loop
*/