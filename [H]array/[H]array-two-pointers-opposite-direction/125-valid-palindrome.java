class Solution {
  public boolean isPalindrome(String s) {
      int left = 0;
      int right = s.length() - 1;
      while (left < right) {
          Character lc = s.charAt(left);
          Character rc = s.charAt(right);
          if (!Character.isLetterOrDigit(lc)) {
              left += 1;
          } else if (!Character.isLetterOrDigit(rc)) {
              right -= 1;
          } else {
              if (Character.toLowerCase(lc) == Character.toLowerCase(rc)) {
                  left += 1;
                  right -= 1;
              } else {
                  return false;
              }
          }
      }
      return true;
  }
}

// time O(n), due to traverse
// space O(1)
// using array and two pointers opposite direction and shrink type