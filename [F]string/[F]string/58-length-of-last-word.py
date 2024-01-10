class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1, - 1, -1):
            if not res and s[i] == ' ':
                continue
            if s[i] == ' ':
                break
            res += 1
        return res
                
# time O(n)
# space O(1)
# using string and traverse from end