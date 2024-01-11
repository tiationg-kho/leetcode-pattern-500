class Solution:
    def isNumber(self, s: str) -> bool:
        met_sign = False
        met_dot = False
        met_num = False
        met_e = False

        for c in s:
            if c in '+-':
                if met_sign or met_dot or met_num:
                    return False
                met_sign = True
            elif c == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif c in 'eE':
                if not met_num or met_e:
                    return False
                met_sign = False
                met_dot = False
                met_num = False
                met_e = True
            elif c.isdigit():
                met_num = True
            else:
                return False
        return met_num

# time O(n)
# space O(1)
# using string and string composition
'''
1. (+/-) (num).num (e/E (+/-) num)
2. (+/-) num (e/E (+/-) num)
'''