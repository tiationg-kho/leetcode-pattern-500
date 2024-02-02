class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, left, right):
            if left == right == n:
                res.append(''.join(path))
                return
            if left < n:
                path.append('(')
                dfs(path, left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                dfs(path, left, right + 1)
                path.pop()

        dfs([], 0, 0)
        return res

# time catalan(n)
# space catalan(n), stack size is O(n)
# using dfs and backtracking and backtracking with constraints