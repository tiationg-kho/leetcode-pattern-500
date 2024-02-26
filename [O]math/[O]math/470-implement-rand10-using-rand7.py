# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1
        
# time O(1) or O(inf)
# space O(1)
# using math and rejection sampling
'''
1. (rand7() - 1) * 7, generate 0,7,14,21,28,35,42
2. after + rand7(), will have random num between 1 - 49 with equal probability
3. then use rejection sampling, if num not in desired range then re-sample it
4. if num in desired range, and inside range every num has same probability, then choose it
'''