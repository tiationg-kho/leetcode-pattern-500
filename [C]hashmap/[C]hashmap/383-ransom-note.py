class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        rchar_freq = [0 for _ in range(26)]
        mchar_freq = [0 for _ in range(26)]
        for c in ransomNote:
            rchar_freq[ord(c) - ord('a')] += 1
        for c in magazine:
            mchar_freq[ord(c) - ord('a')] += 1
        for i in range(26):
            if rchar_freq[i] > mchar_freq[i]:
                return False
        return True
    
# time O(n+m)
# space O(26) == O(1), constant
# using hashmap and store sth’s freq