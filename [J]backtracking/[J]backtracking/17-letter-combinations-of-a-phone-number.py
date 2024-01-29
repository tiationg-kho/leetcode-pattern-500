class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        num_chars = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def dfs(path, idx):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            for c in num_chars[digits[idx]]:
                path.append(c)
                dfs(path, idx + 1)
                path.pop()

        dfs([], 0)
        return res
                
# time O(4**n), n is the length of digits
# space O(n), due to recursion stack, output is O(4**n)
# using dfs and backtracking and backtracking with constraints