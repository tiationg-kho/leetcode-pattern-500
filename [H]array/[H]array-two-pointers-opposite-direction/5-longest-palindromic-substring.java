class Solution {
    public String longestPalindrome(String s) {
        int resLen = 1;
        int resIdx = 0;

        for (int i = 0; i < s.length(); i++) {
            int[] cur = valid(s, i, i);
            if (cur[1] > resLen) {
                resIdx = cur[0];
                resLen = cur[1];
            }
            cur = valid(s, i, i + 1);
            if (cur[1] > resLen) {
                resIdx = cur[0];
                resLen = cur[1];
            }
    }
        return s.substring(resIdx, resIdx + resLen);
    }

    public int[] valid(String s, int left, int right) {
        int[] res = new int[]{left, 1};
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            res[0] = left;
            res[1] = right - left + 1;
            left -= 1;
            right += 1;
        }
        return res;
    }
}

// time O(n**2), traversal costs O(n), and each time need to using two pointers to expand
// space O(1)
// using array and two pointers opposite direction and expand type
/*
1. this is not optimal solution
*/