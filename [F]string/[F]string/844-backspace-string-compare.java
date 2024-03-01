class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1;
        int j = t.length() - 1;
        int iBack = 0;
        int jBack = 0;
        while (i >= 0 || j >= 0) {
            Character iChar = null;
            Character jChar = null;
            while (i >= 0) {
                if (s.charAt(i) == '#') {
                    iBack += 1;
                    i -= 1;
                }
                else if (iBack > 0) {
                    iBack -= 1;
                    i -= 1;
                } else {
                    iChar = s.charAt(i);
                    i -= 1;
                    break;
                }
            }
            while (j >= 0) {
                if (t.charAt(j) == '#') {
                    jBack += 1;
                    j -= 1;
                }
                else if (jBack > 0) {
                    jBack -= 1;
                    j -= 1;
                } else {
                    jChar = t.charAt(j);
                    j -= 1;
                    break;
                }
            }
            if (!Objects.equals(iChar, jChar)) {
                return false;
            }
        }
        return true;
    }
}

// time O(n+m)
// space O(1)
// using string and traverse from end and two pointers