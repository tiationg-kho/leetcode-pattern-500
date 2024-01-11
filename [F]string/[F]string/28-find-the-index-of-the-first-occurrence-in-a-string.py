class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        base = 27
        hashval_set = set()
        hashval = 0
        for i, c in enumerate(needle):
            hashval = hashval * base + ord(c)
        hashval_set.add(hashval)

        hashval = 0
        remove_base = base ** (len(needle) - 1)
        for i, c in enumerate(haystack):
            if i >= len(needle):
                hashval -= remove_base * ord(haystack[i - len(needle)])
            hashval = hashval * base + ord(c)
            if i >= len(needle) - 1:
                if hashval in hashval_set:
                    return i - (len(needle) - 1)
        return - 1

# time O(n+m)
# space O(1)
# using hashmap and rabin karp