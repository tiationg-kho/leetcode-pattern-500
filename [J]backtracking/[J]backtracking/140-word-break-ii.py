class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        res = []
        memo = [True for _ in range(len(s))]

        def dfs(path, idx):
            if idx == len(s):
                res.append(' '.join(path))
                return
            if memo[idx] == False:
                return
            old_res_len = len(res)
            w = ''
            for end in range(idx, len(s)):
                w += s[end]
                if w not in word_set:
                    continue
                path.append(w)
                dfs(path, end + 1)
                path.pop()
            if old_res_len == len(res):
                memo[idx] = False
        
        dfs([], 0)
        return res
    
# time O(2**n), there is 2**n ways to divide input string
# space O(2**n), due to output list
# using dfs and backtracking and backtracking with constraints and prune
'''
1. use memo to prune
2. memo[idx] == False, means substring s[idx:] cannot generate any valid ans
'''