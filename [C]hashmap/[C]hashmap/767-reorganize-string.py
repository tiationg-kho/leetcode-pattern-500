from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1

        char_with_max_freq = max(char_freq.keys(), key=char_freq.get)
        max_freq = char_freq[char_with_max_freq]
        if max_freq > (len(s) + 1) // 2:
            return ''

        res = [None for _ in range(len(s))]
        idx = 0

        def put(char, freq):
            nonlocal idx
            while freq:
                res[idx] = char
                freq -= 1
                idx += 2
                if idx >= len(res):
                    idx = 1
        
        put(char_with_max_freq, max_freq)
        
        for c, f in char_freq.items():
            if c != char_with_max_freq:
                put(c, f)

        return ''.join(res)
        
# time O(n)
# space O(n), due to output list
# using hashmap and store sth’s freq and greedy
'''
1. deal with max freq char first
'''