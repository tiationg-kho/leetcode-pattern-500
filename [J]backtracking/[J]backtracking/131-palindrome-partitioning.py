class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def valid(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(path, idx):
            if idx == len(s):
                res.append(path[:])
                return
            w = ''
            for end in range(idx, len(s)):
                w += s[end]
                if valid(idx, end):
                    path.append(w)
                    dfs(path, end + 1)
                    path.pop()
        
        dfs([], 0)
        return res
    
# time O(2**n * n)
# space O(n)
# using dfs and backtracking and two pointers and backtracking with constraints