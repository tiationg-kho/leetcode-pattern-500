from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        for i, c in enumerate(s):
            if char_freq[c] == 1:
                return i
        return - 1
        
# time O(n), due to traverse twice
# space O(1), due to hashmap (26 letters)
# using hashmap and store sth’s freq