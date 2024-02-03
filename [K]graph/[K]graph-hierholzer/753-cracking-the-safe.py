from collections import defaultdict
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            res = [str(i) for i in range(k)]
            return ''.join(res)

        passwords = []
        def build(path):
            if len(path) == n:
                passwords.append(''.join(path))
                return
            for i in range(k):
                path.append(str(i))
                build(path)
                path.pop()
        build([])

        graph = defaultdict(list)
        for password in passwords:
            p = password[: - 1]
            q = password[1:]
            graph[p].append(q)

        stack = []
        def dfs(node):
            while graph[node]:
                neighbor = graph[node].pop()
                dfs(neighbor)
            stack.append(node)
        dfs('0' * (n - 1))
        
        res = ''
        while stack:
            if not res:
                res += stack.pop()
            else:
                res += stack.pop()[- 1]
        return res
    
# time O(k**n)
# space O(k**n)
# using graph and hierholzer
'''
1. build graph: if n == 3, then 010 can create node 01 and node 10 (and connect them)
'''