/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        int boundary = - 1;
        while (left <= right) {
            int m = left + (right - left) / 2;
            if (isBadVersion(m)) {
                boundary = m;
                right = m - 1;
            } else {
                left = m + 1;
            }
        }
        return boundary;
    }
}

// time O(logn)
// space O(1)
// using binary search and search in sth’s range