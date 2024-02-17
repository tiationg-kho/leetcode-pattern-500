from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        people_balance = defaultdict(int)
        for p, q, w in transactions:
            people_balance[p] += w
            people_balance[q] -= w
        vals = []
        for p, b in people_balance.items():
            if b != 0:
                vals.append(b)
        
        res = float('inf')

        def dfs(count, idx):
            nonlocal res
            if idx == len(vals):
                res = min(res, count)
                return
            if vals[idx] == 0:
                dfs(count, idx + 1)
                return
            for i in range(idx, len(vals)):
                if i == idx:
                    continue
                if vals[idx] * vals[i] >= 0:
                    continue
                settle = vals[idx]
                vals[idx] -= settle
                vals[i] += settle
                count += 1
                dfs(count, idx + 1)
                vals[idx] += settle
                vals[i] -= settle
                count -= 1
        
        dfs(0, 0)
        return res
    
# time O(n!)
# space O(n), due to recursion stack
# using dfs and backtracking and hashmap and backtracking with constraints
'''
1. we are enumerating every possible way to end the debt for each one
'''