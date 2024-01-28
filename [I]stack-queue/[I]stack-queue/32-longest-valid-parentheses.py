class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, left + right)
            elif left < right:
                left, right = 0, 0
        
        left, right = 0, 0
        for i in range(len(s) - 1, - 1, - 1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if right == left:
                res = max(res, right + left)
            elif right < left:
                left, right = 0, 0

        return res
    
# time O(n)
# space O(1)
# using stack and queue and variables to simulate stack
'''
1. first traversal we cannot deal with the potential answer when left > right
2. to fix this, we traverse back to front
'''