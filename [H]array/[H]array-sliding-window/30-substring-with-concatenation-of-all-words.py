from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = defaultdict(int)
        for w in words:
            word_freq[w] += 1
        count_total = len(word_freq)
        
        res = []
        L = len(words[0])
        M = len(words)
        for start in range(L):
            sword_freq = defaultdict(int)
            count = 0
            left = start
            for right in range(start, len(s), L):
                w = s[right: right + L]
                sword_freq[w] += 1
                if sword_freq[w] == word_freq[w]:
                    count += 1
                while right - left + L > L * M or sword_freq[w] > word_freq[w]:
                    remove_w = s[left: left + L]
                    if sword_freq[remove_w] == word_freq[remove_w]:
                        count -= 1
                    sword_freq[remove_w] -= 1
                    if sword_freq[remove_w] == 0:
                        sword_freq.pop(remove_w)
                    left += L
                if count == count_total:
                    res.append(left)
        return res
    
# time O(L * n + m), L is the length of word in words, n is the length of s, and m is the length of words
# space O(m)
# using array and standard sliding window and hashmap
'''
1. enumerate each possible starting point
'''