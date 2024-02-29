class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        schar_freq = [0 for _ in range(26)]
        tchar_freq = [0 for _ in range(26)]
        for c in s:
            schar_freq[ord(c) - ord('a')] += 1
        for c in t:
            tchar_freq[ord(c) - ord('a')] += 1
        for i in range(26):
            if schar_freq[i] != tchar_freq[i]:
                return False
        return True

# time O(n)
# space O(26) == O(1), constant
# using hashmap and store sth’s freq