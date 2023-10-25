class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c not in close_open:
                stack.append(c)
            else:
                if stack and close_open[c] == stack[- 1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

# time O(n)
# space O(n)
# using stack and queue and use stack to store the last states and stack to check (LIFO) and hashmap