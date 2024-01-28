class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
                res.append(c)
            elif c == ')':
                if balance > 0:
                    balance -= 1
                    res.append(c)
            else:
                res.append(c)

        balance = 0
        for i in range(len(res) - 1, - 1, - 1):
            if res[i] == ')':
                balance += 1
            elif res[i] == '(':
                if balance > 0:
                    balance -= 1
                else:
                    res[i] = ''
            else:
                continue

        return ''.join(res)
    
# time O(n), due to traverse twice
# space O(n)
# using stack and queue and variables to simulate stack