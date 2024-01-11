class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        def find(k):
            base = 27
            base2 = 13
            mod = 10**9+7
            hashval_set = set()
            hashval = 0
            hashval2 = 0
            remove_base = (base ** (k - 1)) % mod
            remove_base2 = (base2 ** (k - 1)) % mod
            for i, c in enumerate(s):
                if i >= k:
                    hashval -= (remove_base * ord(s[i - k])) % mod
                    hashval2 -= (remove_base2 * ord(s[i - k])) % mod
                hashval = (hashval * base + ord(c)) % mod
                hashval2 = (hashval2 * base2 + ord(c)) % mod
                if i >= k - 1:
                    if (hashval, hashval2) in hashval_set:
                        return i - (k - 1)
                    hashval_set.add((hashval, hashval2))
            return - 1

        left, right, boundary = 1, len(s) - 1, - 1
        res_idx = - 1
        while left <= right:
            m = (left + right) // 2
            idx = find(m)
            if idx != - 1:
                boundary = m
                res_idx = idx
                left = m + 1
            else:
                right = m - 1
        return s[res_idx: res_idx + boundary] if res_idx != - 1 else ""
        
# time O(nlogn), find() costs O(n) by rolling hash method
# space O(n), due to hashset
# using string and rabin karp and binary search
'''
1. use binary search to guess the length of substring
2. use rolling hash to record is any substring repeated
3. change the length of substring to keep seraching
'''