class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        StringBuffer s = new StringBuffer();
        while (carry > 0 || i >= 0 || j >= 0) {
            if (i >= 0) {
                if (a.charAt(i) == '1') {
                    carry += 1;
                }
                i -= 1;
            }
            if (j >= 0) {
                if (b.charAt(j) == '1') {
                    carry += 1;
                }
                j -= 1;
            }
            int quo = carry / 2;
            int rem = carry % 2;
            if (rem == 1) {
                s.append('1');
            } else {
                s.append('0');
            }
            carry = quo;
        }
        return s.reverse().toString();
    }
}

// time O(max(m, n))
// space O(max(m, n))
// using math