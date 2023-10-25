from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_freq = defaultdict(int)
        res = 0
        left = 0
        for right in range(len(s)):
            char_freq[s[right]] += 1
            while char_freq[s[right]] > 1:
                char_freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        
# time O(n)
# space O(1), due to the hashmap could contain all unique chars
# using array and sliding window and hashmap