from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_lastidx = defaultdict(int)
        for i, c in enumerate(s):
            char_lastidx[c] = i
        
        left = 0
        right = 0
        res = []
        for i in range(len(s)):
            right = max(right, char_lastidx[s[i]])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
                right = i + 1
        return res
                
# time O(n), due to traverse
# space O(1), due to hashmap stores only english letters
# using greedy and hashmap
'''
1. record the last appear idx
'''