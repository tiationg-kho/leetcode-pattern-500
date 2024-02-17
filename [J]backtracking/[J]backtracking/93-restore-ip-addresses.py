class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []

        def dfs(path, idx):
            if idx == len(s) or len(path) == 4:
                if idx == len(s) and len(path) == 4:
                    res.append('.'.join(path))
                return
            if 0 <= int(s[idx]) <= 9:
                path.append(s[idx])
                dfs(path, idx + 1)
                path.pop()
            if 10 <= int(s[idx:idx + 2]) <= 99:
                path.append(s[idx:idx + 2])
                dfs(path, idx + 2)
                path.pop()
            if 100 <= int(s[idx:idx + 3]) <= 255:
                path.append(s[idx:idx + 3])
                dfs(path, idx + 3)
                path.pop()

        dfs([], 0)
        return res

# time O(s * 3**4), s is the length of address (duplicate to output's cost)
# space O(4), due to recursion stack's size, not counting output
# using dfs and backtracking and backtracking with constraints