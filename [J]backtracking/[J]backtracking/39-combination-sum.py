class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path, total, idx):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                total += candidates[i]
                dfs(path, total, i)
                path.pop()
                total -= candidates[i]
        
        dfs([], 0, 0)
        return res
    
# time O(n ** (T/S)), T is target number, and S is the min number in candidates
# space O(T/S), due to recursion stack
# using dfs and backtracking and subset
'''
1. type: subset
2. duplicate elements: no
3. selectable repeatedly: yes
'''