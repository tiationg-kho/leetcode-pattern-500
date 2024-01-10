class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0 for _ in range(len(num1) + len(num2))]

        for i in range(len(num1) - 1, - 1, - 1):
            for j in range(len(num2) - 1, - 1, - 1):
                val = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                idx = len(res) - 1 - (len(num1) - 1 - i + len(num2) - 1 - j)
                res[idx] += val

        carry = 0
        for i in range(len(res) - 1, - 1, - 1):
            carry, res[i] = divmod(res[i] + carry, 10)
        
        num = ''
        for val in res:
            if not val and not num:
                continue
            num += chr(val + ord('0'))
        return num if num else '0'
    
# time O(nm)
# space O(n+m)
# using string and traverse from end and math