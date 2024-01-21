class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(left, right, count):
            while left < right:
                if s[left] != s[right]:
                    if count == 0:
                        return helper(left + 1, right, 1) or helper(left, right - 1, 1)
                    return False
                left += 1
                right -= 1
            return True

        return helper(0, len(s) - 1, 0)

# time O(n), due to traverse
# space O(1)
# using array and two pointers opposite direction and shrink type