class Solution:
    def longestPalindrome(self, s: str) -> str:

        res_len = 0
        res = - 1
        
        for i in range(len(s)):

            left, right = i, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > res_len:
                        res_len = right - left + 1
                        res = left
                    left -= 1
                    right += 1
                else:
                    break
            
            left, right = i, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > res_len:
                        res_len = right - left + 1
                        res = left
                    left -= 1
                    right += 1
                else:
                    break
            
        return s[res: res + res_len]

# time O(n**2), traversal costs O(n), and each time need to using two pointers to expand
# space O(1)
# using array and two pointers opposite direction and expand type
'''
1. this is not optimal solution
'''