class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(path, idx):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(idx, n + 1):
                path.append(i)
                dfs(path, i + 1)
                path.pop()

        dfs([], 1)
        return res
    
# time O(n!/(n-k)!k! * k)
# space O(k), not count output
# using dfs and backtracking and combination
'''
1. type: combination
2. duplicate elements: no
3. selectable repeatedly: no
'''