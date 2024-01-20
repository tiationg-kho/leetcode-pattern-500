from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        res = 0
        left = 0
        for right in range(len(s)):
            char_freq[s[right]] += 1
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    char_freq.pop(s[left])
                left += 1
            res = max(res, right - left + 1)
        return res
                
# time O(n), due to traverse
# space O(k), due to hashmap
# using array and standard sliding window and hashmap