class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        
        first_half = x
        second_half = 0
        while first_half > second_half:
            first_half, remainder = divmod(first_half, 10)
            second_half = second_half * 10 + remainder
            if first_half == second_half:
                return True
            if first_half == second_half // 10:
                return True
        return False

# time O(logn), base 10
# space O(1)
# using math