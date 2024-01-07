from collections import defaultdict
from heapq import *

class FreqWord:
    def __init__(self, f, w):
        self.f = f
        self.w = w

    def __lt__(self, other):
        if self.f == other.f:
            return self.w > other.w
        return self.f < other.f

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = defaultdict(int)
        for w in words:
            word_freq[w] += 1

        heap = []
        for w, f in word_freq.items():
            heappush(heap, FreqWord(f, w))
            if len(heap) > k:
                heappop(heap)
        return [fw.w for fw in sorted(heap, key = lambda x: (- x.f, x.w))]

# time O(nlogk), n is number of words, due to iterate frequency to heap operate
# space O(n + k), due to hashmap to store frequency and heap
# using heap and top k problem (based on heap) and min heap and sort and hashmap
'''
1. use min heap
2. inside heap, we want to pop out the low freq word
3. if same freq, we pop out the large word (so large word must be treated as smaller)
'''