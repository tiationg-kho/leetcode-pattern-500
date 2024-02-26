class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        pos = True if x > 0 else False
        if not pos:
            x = abs(x)
        upper_bound = 2**31 - 1
        lower_bound = - (2**31)

        res = 0
        while x:
            x, remainder = divmod(x, 10)
            if pos and (res > upper_bound // 10 or (res == upper_bound // 10 and remainder > upper_bound % 10)):
                return 0
            if not pos and (- res < int(lower_bound / 10) or (- res == int(lower_bound / 10) and remainder > 10 - lower_bound % 10)):
                return 0
            res = res * 10 + remainder
        
        return res if pos else - res
            
# time O(logn), base 10
# space O(1)
# using math