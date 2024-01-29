class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and stack[- 1] > c and k:
                stack.pop()
                k -= 1
            stack.append(c)
        
        while stack and k:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')
        return res if res else '0'

# time O(n)
# space O(n)
# using stack and queue and montonic and monotonic stack (consider one side’s relationship)
'''
1. 21: when met 1, we pop 2 out and choose 1 to make num smaller
2. 12: when met 1, we cannot pop 1 cause it will make num larger
'''
