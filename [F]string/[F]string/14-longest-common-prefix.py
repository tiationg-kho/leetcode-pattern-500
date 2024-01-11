class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key = len)
        for i, c in enumerate(prefix):
            for s in strs:
                if c != s[i]:
                    return prefix[:i]
        return prefix
    
# time O(nL)
# space O(1)
# using string and string composition
'''
1. notice the order of for loop
'''