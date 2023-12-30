from collections import defaultdict
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        char_leftappear = [None for _ in range(len(s))]
        leftappear = [- 1 for _ in range(26)]
        for i, c in enumerate(s):
            char_leftappear[i] = leftappear[:]
            leftappear[ord(c) - ord('A')] = i

        char_rightappear = [None for _ in range(len(s))]
        rightappear = [len(s) for _ in range(26)]
        for i in range(len(s) - 1, - 1, - 1):
            char_rightappear[i] = rightappear[:]
            rightappear[ord(s[i]) - ord('A')] = i
        
        res = 0
        for i, c in enumerate(s):
            left_bound = char_leftappear[i][ord(c) - ord('A')]
            left_choices = i - left_bound
            right_bound = char_rightappear[i][ord(c) - ord('A')] 
            right_choices = right_bound - i
            res += left_choices * right_choices

        return res

# time O(n)
# space O(n)
# using hashmap's idea
'''
1. think about only consider one char, eg. "AXX'A'XA"
2. use list to sotre the snapshot of hashmap
3. subarray/substring can form by each element's left and right bound/choices
'''