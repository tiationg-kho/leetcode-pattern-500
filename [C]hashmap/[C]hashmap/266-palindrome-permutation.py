from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        
        res = 0
        for c, f in char_freq.items():
            if f % 2 and res % 2:
                return False
            res += f
        return True
    
# time O(n)
# space O(1), due to the number of unique letters
# using hashmap