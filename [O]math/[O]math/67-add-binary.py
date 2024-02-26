class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while carry or i >= 0 or j >= 0:
            if i >= 0:
                if a[i] == '1':
                    carry += 1
                i -= 1
            if j >= 0:
                if b[j] == '1':
                    carry += 1
                j -= 1
            carry, remainder = divmod(carry, 2)
            if remainder == 1:
                res = '1' + res
            else:
                res = '0' + res
        return res    
            
# time O(max(m, n))
# space O(max(m, n))
# using math