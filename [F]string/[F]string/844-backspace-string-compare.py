class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        s_delete, t_delete = 0, 0
        
        while i >= 0 or j >= 0:
            s_char, t_char = None, None

            while i >= 0:
                if s[i] == '#':
                    s_delete += 1
                    i -= 1
                elif s_delete:
                    s_delete -= 1
                    i -= 1
                else:
                    s_char = s[i]
                    i -= 1
                    break

            while j >= 0:
                if t[j] == '#':
                    t_delete += 1
                    j -= 1
                elif t_delete:
                    t_delete -= 1
                    j -= 1
                else:
                    t_char = t[j]
                    j -= 1
                    break

            if s_char != t_char:
                return False
        return True
            
# time O(n+m)
# space O(1)
# using string and traverse from end and two pointers