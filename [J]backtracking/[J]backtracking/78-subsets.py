class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, idx):
            if idx == len(nums):
                res.append(path[:])
                return
            dfs(path, idx + 1)

            path.append(nums[idx])
            dfs(path, idx + 1)
            path.pop()
        
        dfs([], 0)
        return res
    
# time O(n*(2**n)), due to each element can take or not take (2**n), and n for copy list
# space O(n), due to recursion stack, not counting output here
# using dfs and backtracking and subset
'''
1. type: subset
2. duplicate elements: no
3. selectable repeatedly: no
'''
'''
this approach focus on considering each element:
for cur element, 
we don't take, then goto next element
or we take, then goto next element
till no more element to be considered, we record path
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, idx):
            if idx == len(nums):
                res.append(path[:])
                return

            res.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()
        
        dfs([], 0)
        return res
    
# time O(n*(2**n)), due to each element can take or not take (2**n), and n for copy list
# space O(n), due to recursion stack, not counting output here
# using dfs and backtracking and subset
'''
1. type: subset
2. duplicate elements: no
3. selectable repeatedly: no
'''
'''
this approach focus on constructing the path:
record cur path,
then choose a element to add in path

more specific:
we have chosen nothing, record, try to add first element
we have chosen one element, record, try to add another element
we have chosen two elements, record, try to add another element
we have chosen three elements, record, try to add another element
'''