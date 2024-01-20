from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tchar_freq = defaultdict(int)
        for c in s1:
            tchar_freq[c] += 1

        match_total = len(tchar_freq)
        match = 0
        schar_freq = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            schar_freq[s2[right]] += 1
            if schar_freq[s2[right]] == tchar_freq[s2[right]]:
                match += 1
            while right - left + 1 > len(s1):
                if schar_freq[s2[left]] == tchar_freq[s2[left]]:
                    match -= 1
                schar_freq[s2[left]] -= 1
                if schar_freq[s2[left]] == 0:
                    schar_freq.pop(s2[left])
                left += 1
            if match == match_total:
                return True
        return False
    
# time O(m+n)
# space O(1)
# using array and standard sliding window and hashmap