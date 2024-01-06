class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        def valid(k):
            base = 27
            mod = 10**9 + 7
            hashval_set = set()
            hashval = 0
            remove_base = (base ** (k - 1)) % mod
            for i in range(len(s)):
                if i < k:
                    hashval = (hashval * base + ord(s[i])) % mod
                    if i == k - 1:
                        hashval_set.add(hashval)
                else:
                    hashval -= (remove_base * ord(s[i - k])) % mod
                    hashval = (hashval * base + ord(s[i])) % mod
                    if hashval in hashval_set:
                        return True
                    hashval_set.add(hashval)
            return False

        left, right, boundary = 1, len(s) - 1, 0
        while left <= right:
            m = (left + right) // 2
            if valid(m):
                boundary = m
                left = m + 1
            else:
                right = m - 1
        return boundary
    
# time O(nlogn), valid() costs O(n) by rolling hash method
# space O(n), due to list and hashset
# using binary search and search in sth’s range and rabin karp