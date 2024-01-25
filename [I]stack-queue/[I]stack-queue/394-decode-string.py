class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        cur = ''
        num = ''
        for i in range(len(s)):
            if s[i] == '[':
                stack.append((int(num), cur))
                num = ''
                cur = ''
            elif s[i] == ']':
                mul, prev = stack.pop()
                cur = prev + mul * cur
            elif s[i].isdigit():
                num += s[i]
            else:
                cur += s[i]
        return cur
    
# time O(n), not precisely (only true if max freq is small)
# space O(n), not precisely (only true if max freq is small)
# using stack and queue and use stack to store the last states