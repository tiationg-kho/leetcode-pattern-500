class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        res = 0
        left = 0
        for right in range(len(s)):
            if ord(s[right]) - ord(s[left]) == right - left:
                res = max(res, right - left + 1)
            else:
                left = right
        return res
    
# time O(n)
# space O(1)
# using array and two pointers same direction and left ptr to record