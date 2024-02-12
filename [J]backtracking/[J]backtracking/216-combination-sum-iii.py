class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(path, total, idx):
            if total > n:
                return
            if len(path) > k:
                return
            if total == n and len(path) == k:
                res.append(path[:])
                return
            if idx == 10:
                return
            
            for i in range(idx, 10):
                path.append(i)
                total += i
                dfs(path, total, i + 1)
                path.pop()
                total -= i
        
        dfs([], 0, 1)
        return res
    
# time O(9!/(9-k)!k! * k), 9!/(9-k)! is the number of combinations, and k is for copying path
# space O(k)
# using dfs and backtracking and combination
'''
1. type: combination
2. duplicate elements: no
3. selectable repeatedly: no
'''