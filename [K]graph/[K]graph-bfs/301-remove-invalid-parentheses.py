from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def valid(s):
            balance = 0
            for c in s:
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        queue = deque([s])
        res = []
        while queue:
            length = len(queue)
            next_queue = set()
            for _ in range(length):
                string = queue.popleft()
                if valid(string):
                    res.append(string)
                    continue
                for i, c in enumerate(string):
                    if c in '()':
                        next_queue.add(string[: i] + string[i + 1:])
            if res:
                break
            queue.extend(next_queue)

        return res
        
# time O(n * 2**n)
# space O(n * C(2/n, n)), due to the max number of combinations in i round
# using graph and bfs with hashset as queue