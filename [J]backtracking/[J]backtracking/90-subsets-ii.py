class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def dfs(path, visited, idx):
            if idx == len(nums):
                res.append(path[:])
                return

            dfs(path, visited, idx + 1)

            if idx - 1 >= 0 and nums[idx - 1] == nums[idx] and idx - 1 not in visited:
                return
            path.append(nums[idx])
            visited.add(idx)
            dfs(path, visited, idx + 1)
            path.pop()
            visited.remove(idx)

        dfs([], set(), 0)
        return res
    
# time O(2**n * n)
# space O(n)
# using dfs and backtracking and subset and sort
'''
1. type: subset
2. duplicate elements: yes
3. selectable repeatedly: no
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def dfs(path, visited, idx):
            if idx == len(nums):
                res.append(path[:])
                return
            
            res.append(path[:])
            for i in range(idx, len(nums)):
                if i - 1 >= 0 and nums[i - 1] == nums[i] and i - 1 not in visited:
                    continue
                path.append(nums[i])
                visited.add(i)
                dfs(path, visited, i + 1)
                path.pop()
                visited.remove(i)

        dfs([], set(), 0)
        return res

# time O(2**n * n)
# space O(n)
# using dfs and backtracking and subset and sort
'''
1. type: subset
2. duplicate elements: yes
3. selectable repeatedly: no
'''