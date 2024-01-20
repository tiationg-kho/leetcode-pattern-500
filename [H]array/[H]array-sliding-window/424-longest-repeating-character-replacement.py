from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        res = 0
        max_freq = 0
        left = 0
        for right in range(len(s)):
            char_freq[s[right]] += 1
            if char_freq[s[right]] > max_freq:
                max_freq = char_freq[s[right]]
            while max_freq + k < right - left + 1:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    char_freq.pop(s[left])
                left += 1
            res = max(res, right - left + 1)
        return res
    
# time O(n)
# space O(1)
# using array and standard sliding window and hashmap and greedy