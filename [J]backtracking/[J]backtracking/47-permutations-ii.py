class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(path, visited):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i - 1 >= 0 and nums[i - 1] == nums[i] and i - 1 not in visited:
                    continue
                if i not in visited:
                    path.append(nums[i])
                    visited.add(i)
                    dfs(path, visited)
                    path.pop()
                    visited.remove(i)
        
        dfs([], set())
        return res
    
# time O(n! * n)
# space O(n), not count output
# using dfs and backtracking and permutation and sort
'''
1. type: permutation
2. duplicate elements: yes
3. selectable repeatedly: no
'''