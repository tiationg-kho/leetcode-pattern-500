from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0

        for unique_char_count in range(1, 27):
            char_freq = defaultdict(int)
            count = 0
            left = 0
            for right in range(len(s)):
                char_freq[s[right]] += 1
                if char_freq[s[right]] == k:
                    count += 1
                while len(char_freq) > unique_char_count:
                    if char_freq[s[left]] == k:
                        count -= 1
                    char_freq[s[left]] -= 1
                    if char_freq[s[left]] == 0:
                        char_freq.pop(s[left])
                    left += 1
                if count == unique_char_count:
                    res = max(res, right - left + 1)
        return res
    
# time O(n)
# space O(1), due to hashmap
# using array and standard sliding window and hashmap
'''
1-1. when perform naive sliding window, we cannot decide when to move left ptr
1-2. because we do not know how to define the invalid state
2-1. by enumerate how many unique chars should inside the windwow,
2-2. now we know when is valid or invalid (when to move left ptr)
'''