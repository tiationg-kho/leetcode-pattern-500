from collections import defaultdict
class Solution:
    def equalFrequency(self, word: str) -> bool:
        char_freq = defaultdict(int)
        for c in word:
            char_freq[c] += 1
        freq_freq = defaultdict(int)
        for f in char_freq.values():
            freq_freq[f] += 1
        min_freqkey = min(freq_freq.keys())
        max_freqkey = max(freq_freq.keys())
        if len(freq_freq) == 1 and min_freqkey == 1:
            return True
        if len(freq_freq) == 1 and freq_freq[min_freqkey] == 1:
            return True
        if len(freq_freq) != 2:
            return False
        if min_freqkey == 1 and freq_freq[min_freqkey] == 1:
            return True
        if max_freqkey - min_freqkey == 1 and freq_freq[max_freqkey] == 1:
            return True
        return False

# time O(n)
# space O(1)
# using hashmap and store sth’s freq
'''
valid: 1 freq, all freq == 1
valid: 1 freq, (freq) count == 1
valid: 2 freq, small freq == 1 and (small freq) count == 1
valid: 2 freq, large freq == small freq + 1, and (large freq) count == 1
'''