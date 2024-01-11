class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        val_map = {'A':0, 'C':1, 'G':2, 'T':3}
        res = set()
        length = 10
        base = 27
        hashval_set = set()
        hashval = 0
        remove_base = base ** (length - 1)
        for i, c in enumerate(s):
            if i >= length:
                hashval -= remove_base * val_map[s[i - length]]
            hashval = hashval * base + val_map[c]
            if i >= length - 1:
                if hashval in hashval_set:
                    res.add(s[i - (length - 1): i + 1])
                hashval_set.add(hashval)
        return list(res)
    
# time O(n)
# space O(n)
# using string and rabin krap and hashset