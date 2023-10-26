from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        
        res = 0
        for f in char_freq.values():
            if res % 2:
                res += f - (f % 2)
            else:
                res += f
        return res
    
# time O(n)
# space O(n)
# using hashmap and store sth’s freq