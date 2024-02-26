class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while carry or i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1
            carry, remainder = divmod(carry, 10)
            res = chr(remainder + ord('0')) + res
        return res
    
# time O(max(m, n))
# space O(max(m, n))
# using math