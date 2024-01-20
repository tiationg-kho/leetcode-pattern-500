from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pchar_freq = defaultdict(int)
        for c in p:
            pchar_freq[c] += 1
        
        res = []
        match_total = len(pchar_freq)
        match = 0
        schar_freq = defaultdict(int)
        left = 0
        for right in range(len(s)):
            schar_freq[s[right]] += 1
            if schar_freq[s[right]] == pchar_freq[s[right]]:
                match += 1
            while right - left + 1 > len(p):
                if schar_freq[s[left]] == pchar_freq[s[left]]:
                    match -= 1
                schar_freq[s[left]] -= 1
                if schar_freq[s[left]] == 0:
                    schar_freq.pop(s[left])
                left += 1
            if match == match_total:
                res.append(left)
        return res

# time O(m+n), due to traverse
# space O(1), not counting output
# using array and standard sliding window and hashmap