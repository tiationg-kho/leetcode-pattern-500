from collections import defaultdict
import math
class Solution:
    def minSwaps(self, s: str) -> int:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        if abs(char_freq['0'] - char_freq['1']) > 1:
            return - 1
        
        one_first = 0
        zero_first = 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == '0':
                    one_first += 1
                else:
                    zero_first += 1
            else:
                if c == '0':
                    zero_first += 1
                else:
                    one_first += 1
                    
        if char_freq['0'] > char_freq['1']:
            return int(zero_first / 2)
        elif char_freq['0'] < char_freq['1']:
            return int(one_first / 2)
        else:
            return min(int(zero_first / 2), int(one_first / 2))
        
# time O(n)
# space O(1)
# using greedy and hashmap
'''
1. only two types of string's formation
'''