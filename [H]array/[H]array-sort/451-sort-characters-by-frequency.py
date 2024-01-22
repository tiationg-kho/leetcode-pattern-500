from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        
        max_freq = max(char_freq.values())
        min_freq = min(char_freq.values())
        buckets = [[] for _ in range(max_freq - min_freq + 1)]
        for c, f in char_freq.items():
            buckets[f - min_freq].append(c)
        
        res = ''
        for i in range(len(buckets) - 1, - 1, - 1):
            chars = buckets[i]
            for c in chars:
                res += c * (i + min_freq)
        return res

# time O(n + b)
# space O(n + b)
# using array and sort and bucket sort and hashmap