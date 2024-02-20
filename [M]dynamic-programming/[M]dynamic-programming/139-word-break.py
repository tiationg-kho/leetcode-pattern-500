class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for start_idx in range(i):
                if s[start_idx: i] in word_set:
                    dp[i] |= dp[start_idx]
                    
        return dp[len(s)]

# time O(n**3), due to two nested lopp and slice string
# space O(n + m), due to dp list and hashset
# using dynamic programming and linear sequence