class Solution {
    public int myAtoi(String s) {
        boolean metSign = false;
        boolean metNum = false;
        int sign = 1;
        int num = 0;
        int min = Integer.MIN_VALUE;
        int max = Integer.MAX_VALUE;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ' ') {
                if (metSign || metNum) {
                    return sign * num;
                } else {
                    continue;
                }
            } else if (c == '-' || c == '+') {
                if (metSign || metNum) {
                    return sign * num;
                }
                metSign = true;
                if (c == '-') {
                    sign = - 1;
                }
            } else if (Character.isDigit(c)) {
                metNum = true;
                int val = c - '0';
                if (sign * num > max / 10 || (sign * num == max / 10 && sign * val > max % 10)) {
                    return max;
                } else if (sign * num < min / 10 || (sign * num == min / 10 && sign * val < min % 10)) {
                    return min;
                } else {
                    num = num * 10 + val;
                }
            } else {
                return sign * num;
            }
        }
        return sign * num;
    }
}

// time O(n), due to traverse
// space O(1)
// using string and handle value’s bound