from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        char_freq = defaultdict(int)
        bulls, cows = 0, 0
        for sc, gc in zip(secret, guess):
            if sc == gc:
                bulls += 1
                continue
            if char_freq[sc] < 0:
                cows += 1
            if char_freq[gc] > 0:
                cows += 1
            char_freq[sc] += 1
            char_freq[gc] -= 1

        return f'{bulls}A{cows}B'
    
# time O(n)
# space O(1)
# using hashmap
'''
1. positive freq means it appeared more times in the secret
2. negative freq means it appeared more times in the guess
'''