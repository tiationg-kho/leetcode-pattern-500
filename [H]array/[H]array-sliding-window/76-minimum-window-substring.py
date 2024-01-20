from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tchar_freq = defaultdict(int)
        for c in t:
            tchar_freq[c] += 1
        count_total = len(tchar_freq)

        res = float('inf')
        res_idx = - 1
        schar_freq = defaultdict(int)
        count = 0
        left = 0
        for right in range(len(s)):
            schar_freq[s[right]] += 1
            if schar_freq[s[right]] == tchar_freq[s[right]]:
                count += 1
            while count == count_total:
                if right - left + 1 < res:
                    res = right - left + 1
                    res_idx = left
                if schar_freq[s[left]] == tchar_freq[s[left]]:
                    count -= 1
                schar_freq[s[left]] -= 1
                if schar_freq[s[left]] == 0:
                    schar_freq.pop(s[left])
                left += 1
        return s[res_idx: res_idx + res] if res != float('inf') else ''

# time O(m+n)
# space O(1)
# using array and shrink type sliding window and hashmap