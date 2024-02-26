from collections import defaultdict
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        
        res = min(len(s) - char_freq['0'], len(s) - char_freq['1'])
        curchar_freq = defaultdict(int)
        for c in s:
            curchar_freq[c] += 1
            res = min(res, curchar_freq['1'] + char_freq['0'] - curchar_freq['0'])
        return res
        
# time O(n)
# space O(1)
# using greedy and hashmap