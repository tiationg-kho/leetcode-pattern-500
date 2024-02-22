class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0
        for i in range(n):
            dp[i][i] = True
            res += 1
        
        for length in range(2, n + 1):
            for start in range(n):
                end = start + length - 1
                if end >= n:
                    break
                if s[start] == s[end]:
                    cur = True
                    if start + 1 <= end - 1:
                        cur = dp[start + 1][end - 1]
                    dp[start][end] = cur
                    if cur:
                        res += 1
        
        return res

# time O(n**2)
# space O(n**2)
# using dynamic programming and interval (start from short interval)
'''
1. notice that this solution is not the best choice for time complexity
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand(left_center, right_center):
            nonlocal res
            while left_center >= 0 and right_center < n and s[left_center] == s[right_center]:
                res += 1
                left_center -= 1
                right_center += 1
        
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return res

# time O(n**2)
# space O(1)
# using array and two pointers opposite direction and expand type
'''
1. notice that this solution is not the best choice for time complexity
'''