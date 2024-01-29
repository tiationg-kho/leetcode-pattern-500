class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])
                    dfs(path, visited)
                    visited.remove(i)
                    path.pop()
        
        dfs([], set())
        return res
        
# time O(n*n!), dfs will calls n! times and each non-leaf node traverse list costs O(n) and leaf node copy a list to answer costs O(n)
# space O(n*n!), because answer contains n! permutations and each permutaiton can cost O(n). Besides, memory stack size is O(n)
# using dfs and backtracking and permutation
'''
1. type: permutation
2. duplicate elements: no
3. selectable repeatedly: no
'''