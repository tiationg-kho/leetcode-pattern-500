class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in close_open:
                stack.append(c)
            else:
                if not stack or stack[- 1] != close_open[c]:
                    return False
                stack.pop()
        return not stack

# time O(n)
# space O(n)
# using stack and queue and use stack to store the last states and hashmap