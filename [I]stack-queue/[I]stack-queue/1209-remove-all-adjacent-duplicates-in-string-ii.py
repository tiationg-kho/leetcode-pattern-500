class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[- 1][0] != c:
                stack.append([c, 1])
            else:
                stack[- 1][1] += 1
                if stack[- 1][1] == k:
                    stack.pop()
        res = ''
        while stack:
            c, f = stack.pop()
            res = c * f + res
        return res
    
# time O(n), n is the string's length
# space O(n), due to stack
# using stack and queue and use stack to store the last states