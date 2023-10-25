class Solution:
    def romanToInt(self, s: str) -> int:
        char_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and char_val[c] < char_val[s[i + 1]]:
                res -= char_val[c]
            else:
                res += char_val[c]
        return res
        
# time O(n), due to traverse, n is the length of input string
# space O(1), hashmap's size is O(7)
# using hashmap and store val