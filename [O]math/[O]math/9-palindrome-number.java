class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        if (x == 0) {
            return true;
        }
        if (x % 10 == 0) {
            return false;
        }
        int firstHalf = x;
        int secondHalf = 0;
        while (firstHalf > secondHalf) {
            int rem = firstHalf % 10;
            secondHalf = secondHalf * 10 + rem;
            firstHalf /= 10;
        }
        if (firstHalf < secondHalf) {
            secondHalf /= 10;
        }
        return firstHalf == secondHalf;
    }
}

// time O(logn), base 10
// space O(1)
// using math