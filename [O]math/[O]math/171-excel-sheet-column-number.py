class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            res = res * 26 + ord(c) - ord('A') + 1
        return res
        
# time O(n), due to traverse
# space O(1)
# using math