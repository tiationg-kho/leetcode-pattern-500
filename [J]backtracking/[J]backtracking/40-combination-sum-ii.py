class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(path, total, visited, idx):
            if total > target:
                return

            if total == target:
                res.append(path[:])
                return

            if idx == len(candidates):
                return
            
            for i in range(idx, len(candidates)):
                if i - 1 >= 0 and candidates[i - 1] == candidates[i] and i - 1 not in visited:
                    continue
                path.append(candidates[i])
                total += candidates[i]
                visited.add(i)
                dfs(path, total, visited, i + 1)
                path.pop()
                total -= candidates[i]
                visited.remove(i)

        dfs([], 0, set(), 0)
        return res
    
# time O(2**n)
# space O(n), due to recursion stack's size and hashset, not counting output
# using dfs and backtracking and pruning and subset
'''
1. type: subset
2. duplicate elements: yes
3. selectable repeatedly: no
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(path, total, visited, idx):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            if idx == len(candidates):
                return
               
            dfs(path, total, visited, idx + 1)

            if idx - 1 >= 0 and candidates[idx - 1] == candidates[idx] and idx - 1 not in visited:
                return
            path.append(candidates[idx])
            visited.add(idx)
            dfs(path, total + candidates[idx], visited, idx + 1)
            visited.remove(idx)
            path.pop()


        dfs([], 0, set(), 0)
        return res

# time O(2**n)
# space O(n), due to recursion stack's size and hashset, not counting output
# using dfs and backtracking and pruning and subset
'''
1. type: subset
2. duplicate elements: yes
3. selectable repeatedly: no
'''