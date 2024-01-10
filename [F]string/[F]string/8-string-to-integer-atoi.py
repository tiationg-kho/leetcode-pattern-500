class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        num = 0
        max_int = 2**31 - 1
        min_int = - (2**31)

        for c in s:
            if c == ' ' and not sign:
                continue
            elif sign == 0 and c == '+':
                sign = 1
            elif sign == 0 and c == '-':
                sign = - 1
            elif not c.isdigit():
                break
            else:
                if sign == 0:
                    sign = 1
                if sign * num > max_int // 10 or \
                   (sign * num == max_int // 10 and int(c) > max_int % 10):
                    return max_int
                if sign * num < int(min_int / 10) or \
                     (sign * num == int(min_int / 10) and int(c) > 10 - min_int % 10):
                    return min_int
                num = num * 10 + int(c)
            
        return sign * num
        
# time O(n), due to traverse
# space O(1)
# using string and handle value’s bound
'''
-25//10 == -3
int(-25/10) == -2
-102 % 10 == 8
2 == 10 - (-102 % 10)
'''