class Solution:
    def reverseWords(self, s: str) -> str:

        chars = list(' ' + s + ' ')

        def rev(left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        rev(0, len(chars) - 1)

        word = False
        left = 0
        for right in range(len(chars)):
            if chars[right] == ' ' and word:
                rev(left, right)
                word = False
            elif chars[right] != ' ' and not word:
                left = right
                word = True
        
        res = ''
        for c in chars:
            if c != ' ':
                res += c
            elif res and res[- 1] != ' ':
                res += ' '
        return res.rstrip()

# time O(n)
# space O(n)
# using array and two pointers opposite direction and shrink type