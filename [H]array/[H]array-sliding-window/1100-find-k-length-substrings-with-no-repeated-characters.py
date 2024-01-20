from collections import defaultdict
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        res = 0
        left = 0
        for right in range(len(s)):
            char_freq[s[right]] += 1
            while right - left + 1 > k or char_freq[s[right]] > 1:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    char_freq.pop(s[left])
                left += 1
            if len(char_freq) == k:
                res += 1
        return res
    
# time O(n)
# space O(k)
# using array and standard sliding window and hashmap